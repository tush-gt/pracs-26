import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MatrixMultiplication {
    // Input records: A,row,column,value OR B,row,column,value (zero-based indices).
    // For each output cell (i,k), mapper sends matching A(i,j) and B(j,k) records.
    public static class MatrixMapper extends Mapper<LongWritable, Text, Text, Text> {
        @Override
        protected void map(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {
            String line = value.toString().trim();
            if (line.isEmpty()) return;
            String[] p = line.split(",");
            if (p.length != 4) throw new IOException("Bad matrix record: " + line);

            String matrix = p[0].trim();
            int row = Integer.parseInt(p[1].trim());
            int col = Integer.parseInt(p[2].trim());
            double val = Double.parseDouble(p[3].trim());

            Configuration conf = context.getConfiguration();
            int rowsA = conf.getInt("matrix.rowsA", 2);
            int colsA = conf.getInt("matrix.colsA", 5);
            int colsB = conf.getInt("matrix.colsB", 3);

            if ("A".equalsIgnoreCase(matrix)) {
                if (row < 0 || row >= rowsA || col < 0 || col >= colsA)
                    throw new IOException("A coordinate outside declared dimensions: " + line);
                for (int k = 0; k < colsB; k++) {
                    context.write(new Text(row + "," + k), new Text("A," + col + "," + val));
                }
            } else if ("B".equalsIgnoreCase(matrix)) {
                if (row < 0 || row >= colsA || col < 0 || col >= colsB)
                    throw new IOException("B coordinate outside declared dimensions: " + line);
                for (int i = 0; i < rowsA; i++) {
                    context.write(new Text(i + "," + col), new Text("B," + row + "," + val));
                }
            } else {
                throw new IOException("Matrix name must be A or B: " + line);
            }
        }
    }

    public static class MatrixReducer extends Reducer<Text, Text, Text, Text> {
        @Override
        protected void reduce(Text key, Iterable<Text> values, Context context)
                throws IOException, InterruptedException {
            Map<Integer, Double> a = new HashMap<>();
            Map<Integer, Double> b = new HashMap<>();

            for (Text value : values) {
                String[] p = value.toString().split(",");
                int index = Integer.parseInt(p[1]);
                double number = Double.parseDouble(p[2]);
                if ("A".equals(p[0])) a.put(index, number);
                else if ("B".equals(p[0])) b.put(index, number);
            }

            int inner = context.getConfiguration().getInt("matrix.colsA", 5);
            double sum = 0.0;
            for (int j = 0; j < inner; j++) {
                sum += a.getOrDefault(j, 0.0) * b.getOrDefault(j, 0.0);
            }
            context.write(key, new Text(Double.toString(sum)));
        }
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 5) {
            System.err.println("Usage: MatrixMultiplication <input> <output> <rowsA> <colsA> <colsB>");
            System.exit(2);
        }
        Configuration conf = new Configuration();
        conf.setInt("matrix.rowsA", Integer.parseInt(args[2]));
        conf.setInt("matrix.colsA", Integer.parseInt(args[3]));
        conf.setInt("matrix.colsB", Integer.parseInt(args[4]));

        Job job = Job.getInstance(conf, "BDA Matrix Multiplication");
        job.setJarByClass(MatrixMultiplication.class);
        job.setMapperClass(MatrixMapper.class);
        job.setReducerClass(MatrixReducer.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
