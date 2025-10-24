# ===============================================
# TP IA générative : texte poétique en français
# Modèle : GPT-2 français (léger, open source)
# ===============================================

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Pour éviter les problèmes de threads sur certaines machines
torch.set_num_threads(1)

# Nom du modèle léger (Hugging Face Hub)
model_name = "dbddv01/gpt2-french-small"

# Chargement du tokenizer et du modèle
print("Chargement du modèle, cela peut prendre quelques secondes...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()

# Entrée utilisateur
prompt = input("\nEntrez le début de votre poème : ")

# Encodage du texte
inputs = tokenizer(prompt, return_tensors="pt")

# Génération du texte
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=80,      # longueur maximale
        temperature=0.9,        # créativité contrôlée
        top_k=50,               # limitation du vocabulaire
        top_p=0.95,             # nucleus sampling
        do_sample=True,         # génération aléatoire pondérée
        repetition_penalty=1.1  # évite les répétitions
    )

# Décodage du résultat
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("\n--- Poème généré ---\n")
print(generated_text)
