document
  .getElementById("uploadForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    // Dil seçimi
    const lang = document.getElementById("langSelect").value;
    formData.append("lang", lang); // burası çok önemli

    try {
      const response = await fetch("/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      const resultDiv = document.getElementById("result");
      if (data.result && data.result.interpretation) {
        resultDiv.innerHTML = data.result.interpretation.join("<br>");
      } else if (data.error) {
        resultDiv.textContent = "Hata: " + data.error;
      } else {
        resultDiv.textContent = "Beklenmeyen sonuç.";
      }
    } catch (error) {
      document.getElementById("result").textContent =
        "İstek sırasında hata oluştu.";
    }
  });
