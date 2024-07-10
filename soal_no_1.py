def main():
    students = []

    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")

        student = {"NIM": nim, "Nama": nama}
        students.append(student)

        more_data = input("Ingin tambah data? (YA/TIDAK): ").strip().lower()
        if more_data != "ya":
            break

    print("\nData Mahasiswa:")
    for student in students:
        print(f"NIM: {student['NIM']}, Nama: {student['Nama']}")

if __name__ == "__main__":
    main()
