import java.io.IOException;
import java.util.Locale;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class TotalWordCount {
    public static class TotalMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
        private static final Text TOTAL = new Text("Total_Words");
        private final IntWritable count = new IntWritable();

        @Override
        protected void map(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {
            String line = value.toString().toLowerCase(Locale.ROOT)
                    .replaceAll("[^a-z0-9\\s]", " ").trim();
            int words = line.isEmpty() ? 0 : new StringTokenizer(line).countTokens();
            if (words > 0) {
                count.set(words);
                context.write(TOTAL, count);
            }
        }
    }

    public static class TotalReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        private final IntWritable result = new IntWritable();

        @Override
        protected void reduce(Text key, Iterable<IntWritable> values, Context context)
                throws IOException, InterruptedException {
            int total = 0;
            for (IntWritable value : values) total += value.get();
            result.set(total);
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Usage: TotalWordCount <input> <output>");
            System.exit(2);
        }
        Job job = Job.getInstance(new Configuration(), "BDA Total Word Count");
        job.setJarByClass(TotalWordCount.class);
        job.setMapperClass(TotalMapper.class);
        job.setCombinerClass(TotalReducer.class);
        job.setReducerClass(TotalReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
