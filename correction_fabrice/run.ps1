$pythonExe = "C:\Users\ipran\AppData\Local\Programs\Python\Python313\python.exe"

# Chemin du script Python
$scriptPython = "C:\Users\ipran\OneDrive\Bureau\correction_fabrice\code_ploch.py"

# Liste des fichiers CSV à tester
$fichiersCsv = @(
    ".\traiteur.csv"
    ".\test1.csv"
    ".\test2.csv"
    ".\test3.csv"
    ".\test4.csv"
    ".\tést5.csv"
    ".\test6.png"
    ".\test7.webp"

)

foreach ($fichierCsv in $fichiersCsv) {
    if (Test-Path $fichierCsv) {
        Write-Host "Test du fichier $fichierCsv"
        & $pythonExe $scriptPython $fichierCsv
    } else {
        Write-Host "Erreur: Fichier '$fichierCsv' non trouvé!" -ForegroundColor Red
    }
}