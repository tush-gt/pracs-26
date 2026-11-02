import hashlib
import math


class StudentIDBloomFilter:
    def __init__(self, expected_elements=100, false_positive_rate=0.05):
        if expected_elements <= 0:
            raise ValueError("expected_elements must be greater than zero")
        if not 0 < false_positive_rate < 1:
            raise ValueError("false_positive_rate must be between 0 and 1")

        self.n = expected_elements
        self.p = false_positive_rate
        self.size = max(1, math.ceil(
            -(self.n * math.log(self.p)) / (math.log(2) ** 2)
        ))
        self.hash_count = max(1, round(
            (self.size / self.n) * math.log(2)
        ))
        self.bits = [0] * self.size
        self.database = set()

    def _hash_indices(self, item):
        clean = str(item).strip().upper()
        h1 = int(hashlib.md5(clean.encode("utf-8")).hexdigest(), 16)
        h2 = int(hashlib.sha256(clean.encode("utf-8")).hexdigest(), 16)
        return [
            (h1 + i * h2) % self.size
            for i in range(self.hash_count)
        ]

    def possibly_contains(self, item):
        return all(self.bits[index] == 1 for index in self._hash_indices(item))

    def add(self, item):
        clean = str(item).strip().upper()
        if not clean:
            raise ValueError("Student ID cannot be empty")
        for index in self._hash_indices(clean):
            self.bits[index] = 1
        self.database.add(clean)

    def register(self, item):
        clean = str(item).strip().upper()
        if not clean:
            print("Student ID cannot be empty.")
            return
        if self.possibly_contains(clean):
            if clean in self.database:
                print(f"{clean} is already registered.")
                return
            print("Bloom Filter says POSSIBLY PRESENT (false positive possible).")
        self.add(clean)
        print(f"{clean} registered successfully.")

    def check(self, item):
        clean = str(item).strip().upper()
        if not clean:
            print("Student ID cannot be empty.")
            return
        indices = self._hash_indices(clean)
        print("Generated hash indices:", indices)
        if not self.possibly_contains(clean):
            print("DEFINITELY NOT REGISTERED.")
        else:
            print("POSSIBLY REGISTERED.")
            if clean in self.database:
                print("Database verification: record exists (true positive).")
            else:
                print("Database verification: record absent (false positive).")


def main():
    bloom = StudentIDBloomFilter(100, 0.05)

    initial_ids = [
        "2023120045", "2023120032", "2023120047",
        "2023120010", "2023120011", "2023120012",
        "2023120013", "2023120014", "2023120015",
        "2023120016"
    ]
    for student_id in initial_ids:
        bloom.add(student_id)

    while True:
        print("\nSTUDENT ID REGISTRATION CHECKER — BLOOM FILTER")
        print("1. Register a new Student ID")
        print("2. Check a Student ID")
        print("3. View registered IDs (demo database)")
        print("4. Display first 64 bits")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            bloom.register(sid)
        elif choice == "2":
            sid = input("Enter Student ID to check: ").strip()
            bloom.check(sid)
        elif choice == "3":
            print("Registered IDs:")
            for sid in sorted(bloom.database):
                print(sid)
        elif choice == "4":
            print("".join(str(bit) for bit in bloom.bits[:64]))
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
