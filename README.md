# Echoes of Pain Within / Visual Novel 

## Deskripsi Project
Sebuah game dengan genre visual novel, game ini berfokus pada cerita sebagai aspek utama. Dengan tema fantasy superpower. Terdapat pilihan yang mempengaruhi ending/jalan cerita.


## Anggota Kelompok
1. Bintang Renaldy Pratama - [25051204026]
2. Muchammad Achsan Ikhtaru Aufrendi - [25051204028]
3. Klement Ezra Suhartanto - [25051204082]
4. Ibrahim Soffa - [25051204085]

## Fitur Utama
1. Jalan Cerita
2. Pilihan
3. Multi Ending

## Cara Menjalankan Project
1. Run main.py
2. Masuk ke gameplay
3. Melanjutkan jalan cerita

### Prasyarat
Python Pygame

### Instalasi & Menjalankan Game
1. Download file Zip
2. Run main.py
3. Masuk ke gameplay
4. Melanjutkan jalan cerita

## Penjelasan Implementasi OOP

### 1. Encapsulation (Enkapsulasi)
konsep enkapsulasi ini salah satunya berada di BG_manager, yang berada di berbagai class

### 2. Inheritance (Pewarisan)
Semua kelas manajer (termasuk SceneManager) mewarisi kelas Rendering yang berasal dari AbstractRendering/Rendering.py. Artinya, ada kesepakatan bahwa semua class ini adalah turunan dari sistem "penggambar layar", dan mereka wajib tunduk pada aturan atau fungsi dasar yang ada di induknya.

### 3. Polymorphism (Polimorfisme)
SceneManager tidak peduli apakah CurrentNode saat ini sedang berisi kotak dialog, pilihan ganda, atau pemutar video. 
Dia hanya bilang ke CurrentNode untuk menjalankan fungsi render, jika objeknya adalah DialogeBoxManager, fungsi Render() akan menggambar teks mesin tik dan nama karakter.
Jika objeknya adalah ChoiceBoxManager, fungsi Render() akan menggambar deretan tombol vertikal.
Jika objeknya adalah VideoManager, fungsi Render() miliknya sengaja dibiarkan kosong (pass), karena dia hanya fokus mengganti background.
Polimorfisme ini membuat kode SceneManager menjadi sangat pendek dan bersih.

### 4. Abstraction (Abstraksi)
Penerapan konsep abstraksi ini berada di rendering dengan memberikan kata Abstract di fungsi rendering dan juga serialisasi. Contoh deklarasi nya seperti ini 
class DialogeBoxManager(Rendering):

## Screenshot Tampilan Program
===Checkbox_Manager.py
<img width="2291" height="1734" alt="Screenshot 2026-06-04 075529" src="https://github.com/user-attachments/assets/bb0e8567-cc90-4ea7-88e8-86633d5e7bd0" />

===DialogueBox_Manager.py
<img width="2283" height="1734" alt="Screenshot 2026-06-04 075755" src="https://github.com/user-attachments/assets/618bab96-b9e3-4175-a322-6dc85e868cbb" />

===Video_Manager.py
<img width="2320" height="1743" alt="Screenshot 2026-06-04 075845" src="https://github.com/user-attachments/assets/83af1427-c26b-466d-a44f-a69b3fed78c1" />

===Scene_Manager.py
<img width="2306" height="1732" alt="Screenshot 2026-06-04 075923" src="https://github.com/user-attachments/assets/d45028de-a4b9-4294-85c4-df63c8d1c94d" />

===main.py
<img width="2299" height="1764" alt="Screenshot 2026-06-04 075947" src="https://github.com/user-attachments/assets/b028db8a-328b-4d38-b9f1-8f2e1abde51a" />


