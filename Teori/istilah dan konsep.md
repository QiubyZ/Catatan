Berikut adalah beberapa istilah dan konsep yang terkait dalam pemrograman thread:

1. Thread: Unit eksekusi terkecil dalam pemrograman paralel. Thread memungkinkan tugas-tugas yang berbeda untuk dieksekusi secara bersamaan pada CPU yang sama.
2. Proses: Sekumpulan thread yang berjalan dalam konteks yang terpisah dan memiliki sumber daya yang independen. Proses dapat memiliki banyak thread.
3. Multithreading: Pemrograman dengan menggunakan beberapa thread untuk menjalankan tugas-tugas secara paralel. Tujuannya adalah untuk meningkatkan efisiensi dan responsivitas program.
4. Synchronous: Keadaan di mana tugas atau operasi harus menunggu hingga tugas sebelumnya selesai sebelum dapat melanjutkan. Dalam konteks thread, ini mengacu pada thread yang menunggu tugas lain untuk selesai sebelum melanjutkan eksekusinya.
5. Asynchronous: Keadaan di mana tugas atau operasi dapat berlangsung secara bersamaan atau parallel tanpa harus menunggu tugas sebelumnya selesai. Dalam konteks thread, ini mengacu pada thread yang dapat menjalankan tugasnya secara bersamaan dengan thread lain tanpa harus menunggu.
6. Sinkronisasi: Proses mengatur akses dan penggunaan bersama sumber daya atau kode yang sama oleh beberapa thread. Tujuannya adalah untuk mencegah konflik data dan memastikan integritas data.
7. Mutual Exclusion: Pedoman untuk memastikan bahwa hanya satu thread yang dapat mengakses sumber daya yang dibatasi pada satu waktu tertentu. Ini dapat diterapkan menggunakan teknik seperti locking atau mekanisme sinkronisasi lainnya.
8. Deadlock: Situasi di mana dua atau lebih thread saling menunggu satu sama lain karena masing-masing memblokir sumber daya yang dimiliki oleh thread lain, sehingga tidak ada yang bisa melanjutkan eksekusi.
9. Starvation: Situasi di mana satu atau lebih thread tidak mendapatkan akses yang adil terhadap sumber daya yang dibutuhkan. Biasanya terjadi ketika prioritas thread yang lebih rendah selalu diabaikan oleh thread yang lebih tinggi.
10. Race Condition: Masalah yang terjadi ketika dua atau lebih thread mengakses dan memodifikasi sumber daya bersama secara bersamaan, menghasilkan hasil yang tidak konsisten atau tidak diharapkan.
11. Thread Pool: Kumpulan thread yang siap digunakan secara berulang untuk menangani tugas-tugas yang masuk. Thread pool menghindari overhead pembuatan dan penghancuran thread yang berlebihan.
12. Blocking dan Non-Blocking: Blocking mengacu pada keadaan di mana thread yang memanggil suatu operasi tidak bisa melanjutkan sampai operasi tersebut selesai. Non-blocking mengacu pada keadaan di mana thread dapat melanjutkan eksekusinya tanpa harus menunggu.
13. Context Switching: Proses perpindahan dari satu thread ke thread lain. Ini melibatkan menyimpan konteks thread saat ini dan memulihkannya saat thread tersebut dijalankan kembali.
14. Thread Safety: Konsep yang menjamin bahwa operasi pada objek atau kode akan bekerja dengan benar saat dieksekusi oleh beberapa thread secara bersamaan.
15. Joining: Operasi yang memungkinkan thread untuk menunggu hingga thread lain selesai berjalan.

Pemahaman yang baik tentang istilah dan konsep ini akan membantu Anda memahami dan mengelola thread dengan lebih efisien dan aman.
