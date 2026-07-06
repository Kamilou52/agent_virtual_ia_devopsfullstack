import OpenAI from "openai";

const openai = new OpenAI({
        baseURL: 'https://api.deepseek.com',
        apiKey: process.env.DEEPSEEK_API_KEY,
});

async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{ role: "system", content: "You are a helpful assistant Développeur Full-Stack Formateur support IT Agent IA actif." }],
    model: "deepseek-v4-pro",
    thinking: {"type": "enabled"},
    reasoning_effort: "high",
    technical_skills: "high",
    stream: false,
  });

  console.log(completion.choices[0].message.content);
}

main();

function startTraining() {
  alert('Bienvenue! Le module de formation DevOps Full-stack va bientôt être disponible.');
  // À remplacer par la redirection vers le module de formation
  window.location.href = 'training';
}

// Chargement des médias
async function loadProductMedia(productId) {
  const response = await fetch(`/api/product-media/${productId}`);
  const media = await response.json();

  // Génération des thumbnails
  const thumbsContainer = document.querySelector('.gallery-thumbs');
  
  // Images
  media.images.forEach(img => {
    const thumb = document.createElement('img');
    thumb.src = `/assets/products/${img}`;
    thumb.onclick = () => switchMedia('image', img);
    thumbsContainer.append(thumb);
  });

  // Vidéos
  media.videos.forEach(vid => {
    const thumb = document.createElement('div');
    thumb.className = 'video-thumb';
    thumb.innerHTML = '<svg>...</svg>';  // Icône vidéo
    thumb.onclick = () => switchMedia('video', vid);
    thumbsContainer.append(thumb);
  });
}

// Basculer entre médias
function switchMedia(type, src) {
  if(type === 'image') {
    document.getElementById('main-display').src = src;
    document.getElementById('video-player').style.display = 'none';
  } else {
    const player = document.getElementById('video-player');
    player.src = src;
    player.style.display = 'block';
  }
}

