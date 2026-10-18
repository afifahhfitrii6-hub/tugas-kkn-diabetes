// Dataset contoh untuk latihan SPK menggunakan K-Nearest Neighbors (KNN).
// Urutan atribut: usia, BMI, glukosa, tekanan darah, riwayat keluarga (0/1).
const trainingData = [
  { id: "P01", x: [25, 21.5, 90, 110, 0], label: "Rendah" },
  { id: "P02", x: [30, 23.1, 95, 115, 0], label: "Rendah" },
  { id: "P03", x: [35, 25.0, 105, 120, 0], label: "Rendah" },
  { id: "P04", x: [40, 27.5, 120, 125, 1], label: "Tinggi" },
  { id: "P05", x: [45, 30.2, 140, 135, 1], label: "Tinggi" },
  { id: "P06", x: [50, 31.5, 155, 140, 1], label: "Tinggi" },
  { id: "P07", x: [55, 33.0, 165, 145, 1], label: "Tinggi" },
  { id: "P08", x: [28, 22.5, 92, 112, 0], label: "Rendah" },
  { id: "P09", x: [38, 26.8, 115, 122, 0], label: "Rendah" },
  { id: "P10", x: [48, 29.5, 145, 130, 1], label: "Tinggi" }
];

const featureMins = [25, 21.5, 90, 110, 0];
const featureMaxs = [55, 33.0, 165, 145, 1];
const K = 3;

function normalize(value, index) {
  return (value - featureMins[index]) / (featureMaxs[index] - featureMins[index] || 1);
}

function euclideanDistance(input, row) {
  const squaredSum = input.reduce((sum, value, index) => {
    const difference = normalize(value, index) - normalize(row.x[index], index);
    return sum + difference * difference;
  }, 0);
  return Math.sqrt(squaredSum);
}

function classifyPatient(input) {
  const nearest = trainingData
    .map(row => ({ id: row.id, label: row.label, distance: euclideanDistance(input, row) }))
    .sort((a, b) => a.distance - b.distance)
    .slice(0, K);

  const highCount = nearest.filter(row => row.label === "Tinggi").length;
  const lowCount = nearest.length - highCount;
  // Jika terjadi seri, program memilih Rendah. Dengan K=3 dan dua label, seri tidak terjadi.
  const label = highCount > lowCount ? "Tinggi" : "Rendah";
  return { label, nearest, highCount, lowCount };
}

function showResult(result) {
  const resultBox = document.getElementById("result");
  resultBox.className = "result-box " + (result.label === "Tinggi" ? "high" : "low");
  resultBox.innerHTML = `
    <div class="result-icon">${result.label === "Tinggi" ? "!" : "✓"}</div>
    <div class="result-label">Hasil klasifikasi KNN</div>
    <div class="result-title">Risiko ${result.label}</div>
    <div class="result-detail">
      Dari ${K} tetangga terdekat, <b>${result.highCount}</b> berlabel Tinggi dan
      <b>${result.lowCount}</b> berlabel Rendah.<br>
      Data terdekat: ${result.nearest.map(row => `${row.id} (${row.label})`).join(", ")}.
    </div>`;
}

const form = document.getElementById("patientForm");
const resetButton = document.getElementById("resetBtn");

form.addEventListener("submit", event => {
  event.preventDefault();
  const input = [
    Number(document.getElementById("age").value),
    Number(document.getElementById("bmi").value),
    Number(document.getElementById("glucose").value),
    Number(document.getElementById("bp").value),
    Number(document.getElementById("family").value)
  ];

  if (input.some(value => !Number.isFinite(value))) {
    alert("Periksa kembali data yang dimasukkan.");
    return;
  }
  showResult(classifyPatient(input));
});

resetButton.addEventListener("click", () => {
  document.getElementById("age").value = 42;
  document.getElementById("bmi").value = 28.5;
  document.getElementById("glucose").value = 130;
  document.getElementById("bp").value = 128;
  document.getElementById("family").value = "1";
  const resultBox = document.getElementById("result");
  resultBox.className = "result-box empty";
  resultBox.innerHTML = '<div class="result-icon">●</div><b>Hasil akan muncul di sini</b><span class="result-note">Tekan tombol “Hitung Prediksi Risiko”.</span>';
});
