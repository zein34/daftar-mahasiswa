<!DOCTYPE html>
<html leng = "en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <title>Index</title>
  </head>

  <body>
    <a href ="/tambah">+ tambah</a>

    <table border = "1" solid black>
        <tr>
          <th colspan = "3">Daftar Mahasiswa</th>
        </tr>
        <th>Nama</th>
        <th>NIM</th>
        <th>Jurusan</th>

        {% for baris in data: %}
          <tr>
            <td>{{ baris[1] }}</td>
            <td>{{ baris[2] }}</td>
            <td>{{ baris[3] }}</td>
            <td>
              <a href = "/delete/{{ baris[0] }}">Hapus</a>
              <a href = "/edit/{{ baris[0] }}">Ubah</a>
            </td>
          </tr>
        {% endfor %}
  </body>
</html>
