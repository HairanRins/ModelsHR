document.getElementById("predictionForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const month = document.getElementById("month").value;

    // Requête AJAX pour récupérer les prédictions
    const response = await fetch(`/predict?month=${month}`);
    const result = await response.json();

    // Afficher les résultats
    document.getElementById("result").innerHTML = `
        <p><strong>Mois :</strong> ${month}</p>
        <p><strong>Prédiction du taux :</strong> ${result.prediction.toFixed(2)}</p>
    `;
});
