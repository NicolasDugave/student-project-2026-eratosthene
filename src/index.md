---
layout: default
toc: false
---


<style>
  @import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Serif:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Yeseva+One&display=swap");

  /* --- GESTION DES SCROLLS ET DU COMPORTEMENT GLOBAL --- */
  
  :root {
    /* Écrase la variable interne d'Observable qui restreint la largeur et crée la zone blanche */
    --observablehq-max-width: 100% !important; 
  }

  html, body {
    overflow-x: hidden !important; /* Supprime le slider glisseur du bas (gauche/droite) */
    overflow-y: auto !important;   /* Conserve le défilement de haut en bas si nécessaire */
    margin: 0 !important;
    padding: 0 !important;
    width: 100vw !important;
  }

  /* --- SIDEBAR FIXE À INTERDIRE LE REPLI (10%) --- */
  
  .observablehq-sidebar, #observablehq-sidebar {
    width: 16vw !important;
    min-width: 12vw !important;
    max-width: 16 !important;
    position: fixed !important;
    left: 0 !important;
    top: 0 !important;
    height: 100vh !important;
    box-sizing: border-box;
    z-index: 1000;
  }

  /* Cache le bouton "hamburger" de repli s'il persiste dans le DOM HTML */
  .observablehq-sidebar-toggle, button[aria-label="Toggle sidebar"] {
    display: none !important;
  }

  /* --- ZONE CONTENU PRINCIPAL À DROITE (90%) --- */
  
  .observablehq-main {
    width: 90vw !important;
    max-width: 90vw !important;
    margin-left: 10vw !important; /* Décalage strict aligné sur la sidebar */
    margin-right: 0 !important;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
    padding: 0 !important;
    box-sizing: border-box;
    min-height: 100vh !important;
    display: flex !important;
    flex-direction: column !important;
  }

  /* --- CONTENEUR APPLICATION (MAP + SLIDER) --- */
  
.tm-container {
  width: 100% !important;
  max-width: 100% !important;
  height: auto !important; /* On retire le 100vh qui étirait artificiellement le conteneur */
  margin: 0 !important;
  padding: 0 !important; /* On supprime le padding qui créait du vide autour de la carte */
  display: flex !important;
  flex-direction: column !important;
}

#map {
  position: relative;
  height: 65vh !important; /* On fixe proprement la hauteur de la carte */
  width: 100% !important;
  margin-bottom: 0 !important; /* Force le bandeau du slider à coller à la carte */
}

/* On cible le bandeau du slider (celui qui a la classe py-12 ou py-4) */
.tm-container > div.w-full {
  padding-top: 10px !important;    /* Espace minimal au-dessus du slider */
  padding-bottom: 15px !important; /* Espace minimal en-dessous du slider */
  margin: 0 !important;
}

/* --- SUPPRESSION DES MARGES DU TEXTE D'INTRO --- */

#intro-texte {
  margin-top: 0 !important;
  padding-top: 15px !important;    /* Le texte se colle juste sous le bandeau du slider */
  padding-bottom: 15px !important; 
}

/* Ajustement de la zone principale pour qu'elle ne force pas un étirement vertical vide */
.observablehq-main {
  width: 90vw !important;
  max-width: 90vw !important;
  margin-left: 10vw !important;
  padding: 0 !important;
  min-height: 100vh !important;
  display: block !important; /* Repasse en block pour que le texte suive naturellement le flux sans s'écarter */
}

  /* --- ZONE SLIDER D'ANNÉE --- */
  
  #year-slider {
    -webkit-appearance: none;
    width: 100%;
    background: #3f3f46;
    height: 12px;
    border-radius: 999px;
    outline: none;
    margin-top: 15px !important;
    margin-bottom: 0 !important;
    padding: 0;
    cursor: pointer;
  }

  .slider-label-container {
    display: flex;
    justify-content: space-between;
    width: 100%;
    padding: 0 5px;
    margin-top: 8px;
    margin-bottom: 5px;
    box-sizing: border-box;
  }

  /* --- COMPORTEMENT WRAPPER OBSERVABLEHQ --- */
  
  .observablehq {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  /* --- LEAFLET CUSTOM POPUPS --- */
  
  .leaflet-popup-content-wrapper {
    border-radius: 8px !important;
    padding: 4px !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.4) !important;
  }
  .leaflet-popup-content {
    margin: 10px 12px !important;
  }
  .custom-popup h3 {
    margin-bottom: 2px;
  }

  /* --- AUGMENTATION DE LA POLICE DANS LA SIDEBAR --- */

/* Cible les liens des pages principales dans la sidebar */
.observablehq-sidebar a, 
#observablehq-sidebar a {
  font-size: 1.2rem !important; /* Augmente la taille (par défaut ~0.85rem-0.9rem) */
  font-weight: 500 !important;  /* Donne un peu plus d'épaisseur pour la lisibilité */
}

/* Cible les titres de sections si vous en avez (ex: "Navigation") */
.observablehq-sidebar h3,
.observablehq-sidebar-section-header,
#observablehq-sidebar .observablehq-sidebar-heading {
  font-size: 1.3rem !important; /* Légèrement plus grand pour les titres de sections */
  font-weight: 700 !important;
  color: #ffffff !important;    /* Force un blanc pur pour que ça ressorte bien */
}

/* Ajuste l'espacement pour éviter que les textes plus grands ne se chevauchent */
.observablehq-sidebar li, 
#observablehq-sidebar li {
  margin-top: 8px !important;
  margin-bottom: 8px !important;
}

/* --- STYLE DE L'ENCADRÉ LÉGENDE DE LA CARTE --- */

.legend-box {
  background: rgba(255, 255, 255, 0.95) !important; /* Fond blanc pur légèrement translucide */
  padding: 12px 16px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
  font-family: 'Poppins', 'Helvetica Neue', Arial, sans-serif !important;
  color: #1f2937 !important; /* Texte gris très foncé (presque noir) pour un contraste maximal */
  min-width: 150px;
}

.legend-title {
  margin: 0 0 8px 0 !important;
  font-size: 14px !important;
  font-weight: 700 !important;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #111827 !important;
  border-b: 1px solid #e5e7eb;
  padding-bottom: 4px;
}

.legend-item {
  display: flex !important;
  align-items: center !important;
  margin-bottom: 6px !important;
  font-size: 13px !important;
  font-weight: 500 !important;
}

.legend-item:last-child {
  margin-bottom: 0 !important;
}

/* Représentation sous forme de ligne épaisse (comme vos tracés de lignes) */
.legend-line {
  display: inline-block !important;
  width: 24px !important;
  height: 4px !important;
  border-radius: 2px !important;
  margin-right: 10px !important;
  flex-shrink: 0;
}

  /* --- HARMONISATION ET PASSAGE EN FORCE DE LA TYPOGRAPHIE --- */

  /* 1. Les grandes dates d'en-tête (ex: 1873) */
  .article-historique .date-majeure-index,
  .article-historique div[class*="text-red-600"] {
    color: #e31a1c !important;
    font-weight: 900 !important;
    font-size: 2rem !important; /* text-2xl */
    font-family: 'Poppins', sans-serif !important;
    margin-bottom: 0.5rem !important;
  }

  /* 2. Les titres d'événements */
  .article-historique h2 {
    font-size: 2.25rem !important; /* text-4xl */
    font-weight: 900 !important;    /* font-black */
    font-style: italic !important;   /* italic */
    margin-bottom: 2.5rem !important; /* mb-10 */
    color: #18181b !important;      /* text-zinc-900 */
  }

  /* Ajustement de la taille du titre pour les écrans d'ordinateurs (md:) */
  @media (min-width: 768px) {
    .article-historique h2 {
      font-size: 3rem !important; /* md:text-5xl */
    }
  }

  /* 3. Les paragraphes de récit (Identique à la page analyse) */
  .article-historique p {
    font-size: 1.2rem !important; /* text-xl */
    font-weight: 500 !important;    /* font-medium */
    line-height: 1.5 !important;  /* Ajusté légèrement pour le confort de lecture du sans-serif */
    color: #71717a !important;      /* text-zinc-500 */
    text-align: justify !important; /* Texte justifié */
    text-justify: inter-word !important;
    margin: 0 !important;
    margin-bottom: 1.2rem !important; /* Maintient l'espace respirable entre paragraphes */
  }

  /* 4. Les listes à puces (Bullet Points) harmonisées */
  .article-historique ul.list-disc {
    font-family: 'Poppins', sans-serif !important;
    font-size: 1.1rem !important;
    line-height: 1.6 !important;
    color: #71717a !important;
    margin-bottom: 1.5rem !important;
    padding-left: 2rem !important;
  }
  .article-historique ul.list-disc li {
    margin-bottom: 0.75rem !important;
  }
  .article-historique ul.list-disc strong {
    font-weight: 700 !important;
    color: #111827 !important; /* Fait ressortir le sujet de la puce */
  }

  /* 5. Les légendes sous les images */
  .article-historique .mt-12 p, 
  .article-historique div[class*="md:w-1/2"] p.italic {
    font-family: 'Poppins', sans-serif !important;
    font-size: 0.875rem !important;
    color: #71717a !important;
    font-style: italic !important;
    text-align: right !important;
    margin-top: 0.5rem !important;
  }

  .titre-evenement {
  font-size: 2.25rem !important; /* text-4xl */
  font-weight: 900 !important;    /* font-black */
  font-style: italic !important;   /* italic */
  margin-bottom: 2.5rem !important; /* mb-10 */
  color: #18181b !important;      /* text-zinc-900 */
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
}
/* Ajustement responsive pour le titre */
@media (min-width: 768px) {
  .titre-evenement {
    font-size: 3rem !important; /* md:text-5xl */
  }
}

</style>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.8.0/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.8.0/dist/leaflet.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.9.2/proj4.js"></script>
<script src="https://cdn.tailwindcss.com"></script>

</script>

<div class="tm-container bg-zinc-800" id="top-of-page">
  
  <div class="px-8 py-6 flex justify-between items-center text-white border-b border-zinc-700">
    <div class="w-1/3">
      <!-- Correction : Remplacement de font-thin par font-bold ou font-medium pour donner de l'impact visuel à la date -->
      <h1 id="date-text" class="text-7xl font-bold text-white tracking-tight">1907</h1>
    </div>
    <div class="text-right">
      <!-- Correction : Remplacement de la classe invalide font-white par text-white (blanc pur éclatant) -->
      <h2 class="text-4xl md:text-5xl italic font-serif text-white drop-shadow-md">Lausanne Time Machine</h2>
      <p class="text-sm font-light not-italic text-zinc-300">
        Une histoire géographique du développement des transports publics dans le centre ville de Lausanne.
      </p>
    </div>
  </div>

  <div id="map" class="bg-black"></div>

  <div class="py-4 bg-zinc-900 w-full">
    <div class="w-11/12 md:w-5/6 mx-auto relative px-0"> 
      <input 
        type="range" 
        id="year-slider" 
        min="0" 
        max="6" 
        step="1" 
        value="6"
      >
      <div class="slider-label-container text-zinc-400 text-sm md:text-2xl font-black">
        <span class="w-0 flex justify-center whitespace-nowrap">1907</span>
        <span class="w-0 flex justify-center whitespace-nowrap">1925</span>
        <span class="w-0 flex justify-center whitespace-nowrap">1937</span>
        <span class="w-0 flex justify-center whitespace-nowrap">1973</span>
        <span class="w-0 flex justify-center whitespace-nowrap">1983</span>
        <span class="w-0 flex justify-center whitespace-nowrap">2000</span>
        <span class="w-0 flex justify-center whitespace-nowrap">2025</span>
      </div>
    </div>
  </div>
</div>

<div class="tm-container py-16 text-white font-sans mt-10 w-90vw">

<div id="leb-1873" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">1873</div>
  <h2>Un train suburbain : le chemin de fer Lausanne-Échallens-Bercher (LEB)</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        Le Chemin de fer Lausanne-Échallens-Bercher (LEB), surnommé historiquement la « Brouette », a radicalement transformé sa vocation, passant d’un train à vapeur agricole à un véritable RER suburbain de haute fréquence. Inauguré sur son premier tronçon en 1873, il relie Lausanne à Bercher dès 1889, jouant initialement un rôle vital pour l'acheminement des denrées du Gros-de-Vaud, notamment le lait et les betteraves, vers la capitale. L’électrification de la ligne en 1935 marque une première étape cruciale vers la modernisation technique.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">29</sup> Toutefois, c'est l'explosion démographique de l'arrière-pays lausannois à la fin du XXe siècle qui redéfinit son utilité publique.
      </p>
      <p>
        Sa fréquentation a ainsi bondi, passant de 1,5 million de passagers en 1995 à plus de 4 millions annuels aujourd'hui, selon les derniers rapports d’activité des tl qui assurent sa gestion opérationnelle depuis 2013. L’étape la plus marquante de ce début de siècle demeure l’inauguration, en mai 2022, du tunnel de 1,7 kilomètre sous l’avenue d’Échallens. Ce projet titanesque de 190 millions de francs a permis de supprimer le tronçon routier le plus accidentogène du réseau et d'instaurer une cadence à dix minutes.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">30</sup> Désormais totalement intégré au pôle d'échanges de Lausanne-Flon, le LEB agit comme une extension septentrionale du métro, fusionnant la portée d'un chemin de fer régional avec l'efficacité d'un transport urbain lourd.
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/leb-1873.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="LEB historique et tunnel" />
      <p class="italic">Les premières voitures en 1873, Collection tl<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">34</sup></p>
    </div>
  </div>
</div>

<div id="ficelle-1877" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">1877</div>
  <h2>L'émergence de la "Ficelle" et la genèse du transport vertical</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        Le premier jalon fondamental de l'histoire des transports lausannois est posé bien avant l'avènement de l'électricité, avec la mise en service du funiculaire Lausanne-Ouchy (LO) le 16 mars 1877.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">2</sup> À cette époque, la gare ferroviaire, inaugurée en 1858, est située "dans les vignes", à mi-distance entre le port d'Ouchy et le centre-ville.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup> Le besoin de relier ces trois pôles économiques devient une priority absolue pour les édiles lausannois. L'infrastructure fut imposée par l'obsolescence des transports hippomobiles face à l'essor du fret ferroviaire. Le projet permit surtout la valorisation foncière du Flon : ses marécages furent comblés pour accueillir un port franc et des entrepôts, ancrant la logistique au cœur de la cité. Cette jonction visait également à désenclaver Ouchy pour le tourisme et à favoriser l'extension urbaine vers le sud.
      </p>
      <p>
        Ce funiculaire, rapidement surnommé "La Ficelle" par les habitants, représente alors une prouesse technique majeure, utilisant la gravité et l'énergie hydraulique pour vaincre la pente. En 1879, un second tronçon, le Lausanne-Gare (LG), is inauguré parallèlement au premier pour relier spécifiquement la gare CFF au quartier du Flon.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">2</sup> Ce système bifide devient l'épine dorsale de la ville. La gestion de ce réseau est confiée à la Société du Chemin de fer Lausanne-Ouchy, qui exploite une infrastructure dont les caractéristiques techniques préfigurent déjà les performances du futur métro M2. La transition technologique s'opère progressivement : après plusieurs décennies d'exploitation hydraulique, le LG est converti en chemin de fer à crémaillère en octobre 1954, suivi par le LO en mai 1958.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">2</sup>
      </p>
      <p>
        L'importance de la "Ficelle" dépasse le simple transport de voyageurs. Pendant près d'un siècle, elle assure également le trafic de marchandises entre le port et les entrepôts du Flon. En 1964, année de l'Exposition nationale, le trafic atteint des sommets avec 9,5 millions de passagers, avant de se stabiliser autour de 7 millions dans les années suivantes.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">1</sup> Ce système, bien que technologiquement dépassé à la fin du XXe siècle, a durablement ancré l'idée d'un axe fort nord-sud totalement indépendant de la circulation routière.
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/ficelle.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="La Ficelle" />
      <p class="italic">Vue du funiculaire Lausanne-Ouchy non datée, Collection Martine Desarzens</p>
    </div>
  </div>
</div>

<div id="tramways-1896" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">1896</div>
  <h2>La révolution électrique et la naissance des Tramways Lausannois</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        Si le funiculaire a résolu la liaison verticale, le développement horizontal de la ville nécessite une technologie plus flexible. Le 5 juin 1895 est créée la Société des tramways lausannois (TL), sous l'impulsion de l'ingénieur Adrien Palaz.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">5</sup> Contrairement à d'autres métropoles européennes qui hésitent encore entre la vapeur et l'air comprimé, Lausanne opte d'emblée pour la traction électrique, malgré les défis posés par ses pentes importantes.
      </p>
      <p>
        Le réseau est inauguré le 29 août 1896 et entre en service régulier le 1er septembre 1896 avec six lignes initiales couvrant 7,2 kilomètres.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup> Pour alimenter ces motrices, une centrale électrique dédiée est édifiée à Couvaloup, entre la rue Saint-Martin et l'école de médecine, dès août 1895.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup> Elle sert également de premier dépôt-atelier pour les 14 premières automotrices.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">6</sup>
      </p>
      <p>
        L'audace technique est particulièrement visible sur la ligne de la Pontaise, qui présente une rampe maximale de 12%, une valeur record pour un système de tramway à simple adhérence.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">6</sup> Cette caractéristique oblige les ingénieurs à concevoir des systèmes de freinage redondants et particulièrement puissants. L'impact social est immédiat : les lignes rapprochent les quartiers périphériques du centre politique et économique de Saint-François, favorisant une densification urbaine sans précédent.
      </p>
      <p>
        L'année 1896 marque donc le passage de Lausanne du statut de bourgade fragmentée à celui d'agglomération moderne. Les cadences, fixées à 10 minutes en journée, imposent un rythme nouveau à la vie citadine.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">7</sup> Le succès est tel qu'un second dépôt plus vaste doit être construit à Prélaz entre 1898 et 1900 pour abriter un parc roulant qui ne cesse de croître.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup>
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/plan-tramways-1896.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Plan et tramway lausannoi" />
      <p class="italic" style="margin-bottom: 1.5rem;">Plan du réseau (1959)</p>
      <img src="static/img/tramways-1896.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Plan et tramway lausannois" />
      <p class="italic">Premier tramway (1895)<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">36</sup></p>
    </div>
  </div>
</div>

<div id="signal-1899" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">1899</div>
  <h2>Inauguration du funiculaire Lausanne-Signal</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        Inauguré le 18 octobre 1899, le funiculaire Lausanne-Signal constitue la troisième infrastructure à câble de la ville, conçue pour relier le quartier du Vallon au belvédère du Signal de Sauvabelin, alors haut lieu du tourisme local. Longue de 468 mètres avec un dénivelé de 113 mètres, cette ligne affichait une rampe maximale de 28 % et se distinguait techniquement par l'usage immédiat de la traction électrique, contrairement au Lausanne-Ouchy initialement mû par contrepoids hydraulique. Porté par la Société du Funiculaire Lausanne-Signal, le projet visait à faciliter l'accès à cette colline boisée dont l'ascension était jugée pénible pour les promeneurs et les curistes.
      </p>
      <p>
        En termes d'exploitation, le funiculaire transportait environ 100 000 passagers par an dans ses meilleures années, mais sa rentabilité déclina inexorablement avec l'essor de la mobilité routière et l'évolution des loisirs. Malgré son utilité ludique, le service fut définitivement interrompu le 31 octobre 1948, victime de la concurrence des lignes d'autobus plus flexibles, notamment l'actuelle ligne 16 des tl. La fermeture de cette infrastructure marque une étape clé de la transition vers le transport sur pneus de l'après-guerre. Aujourd'hui, les vestiges de la gare supérieure au Signal, transformée en habitation privée, ainsi que l'ancienne tranchée visible dans la pente du Vallon, demeurent les derniers témoins matériels de cette liaison pittoresque dont la concession n'a jamais été renouvelée.
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/affiche-1899.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Affiche et vue du funiculaire" />
      <p class="italic" style="margin-bottom: 1.5rem;">Affiche publicitaire du Signal de Sauvabelin vers 1900, Musée historique de Lausanne<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">37</sup></p>
      <img src="static/img/vue-1899.webp" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Affiche et vue du funiculaire" />
      <p class="italic">Vue du funiculaire Lausanne-Signal vers 1940, Collection Martine Desarzens<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">33</sup></p>
    </div>
  </div>
</div>

<div id="bus-1920" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">1920</div>
  <h2>L’apparition des premières lignes de bus privées</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        L'apparition des premières lignes d'autobus à Lausanne au milieu des années 1920 marque une étape charnière dans l'histoire des transports urbains, signalant la fin de l'hégémonie exclusive du rail (tramway). À cette époque, la Société des Tramways Lausannois (tl) et des entrepreneurs privés cherchent à desservir des zones inaccessibles au tram en raison de la topographie ou d'une rentabilité insuffisante pour la pose de rails.
      </p>
      <p>
        L'une des lignes les plus emblématiques de cette période est celle de Saint-Sulpice, lancée initialement par une entreprise privée vers 1924-1925 pour relier le centre de Lausanne aux plages et aux zones résidentielles de l'Ouest lausannois. Cette ligne, qui longeait le lac, fut finalement reprise par les TL en 1929. Parallèlement, la desserte du quartier de la Cité représentait un défi technique majeur : les rues étroites et les pentes escarpées du cœur historique empêchaient l'installation de rails de tramway.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">29</sup> Pour y remédier, des services d'autobus légers gérés par des concessionnaires ont commencé à circuler dès le milieu des années 20, préfigurant la création officielle de la "Ligne de la Cité" gérée par les TL en 1930. Ces bus permettaient une liaison directe entre la Place Saint-François et le sommet de la colline de la Cité, longeant la Cathédrale.
      </p>
      <p>
        Cette diversification du parc roulant illustre la volonté de Lausanne de devenir un laboratoire de mobilité, utilisant l'autobus comme un complément flexible au réseau de tramways alors à son apogée (66 km de voies).
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/bus-1920.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Place de la Palud" />
      <p class="italic">Place de la Palud, entre 1916 et 1928, Collection Martine Desarzens au Musée Historique de Lausanne<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">33</sup></p>
    </div>
  </div>
</div>

<div id="trolleybus-1932" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">1932</div>
  <h2>Le tournant de 1932 : Le trolleybus comme réponse au relief</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        Malgré le succès des tramways, les contraintes de maintenance des voies ferrées sur des terrains instables et des pentes fortes commencent à peser sur les finances de la compagnie. En 1931, Lausanne décide d'expérimenter une technologie émergente : le trolleybus moderne.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup> La première ligne d'essai est inaugurée en 1932 entre la gare CFF et Ouchy via l'avenue de la Harpe.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup>
      </p>
      <p>
        Ce choix technologique est motivé par plusieurs facteurs critiques. La section entre le Closelet et les Épinettes, auparavant exploitée par tramway, présentait des coûts d'exploitation prohibitifs en raison de l'usure prématurée des rails et des systèmes de freinage.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup> Le trolleybus, avec ses pneumatiques, offre une meilleure adhérence sur chaussée humide et une souplesse de conduite supérieure dans le trafic automobile naissant. Le premier modèle mis en service, le TL-2 construit par FBW, donne des résultats jugés "excellent" par la direction des TL.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup>
      </p>
      <p>
        Cette réussite marque le début d'une politique de substitution systématique. Convaincus par la performance du système, les TL commandent une série de 32 trolleybus de conception lausannoise, reconnaissables à leur capot proéminent à l'avant.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup> Entre 1938 et 1939, cinq lignes de tramway sont supprimées et remplacées par des trolleybus.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup> Le mouvement vers le "tout-pneu" est lancé, soutenu par une partie de la population qui voit dans le rail un vestige du XIXe siècle, encombrant pour la circulation des voitures individuelles.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">7</sup> En 1948, une étape politique majeure survient : la population refuse par votation le rachat de la compagnie par la ville de Lausanne, laissant aux TL une autonomie de gestion qui favorisera l'expansion du réseau routier au détriment du rail.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">3</sup>
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/accident-1932.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Accident de tramway et premier trolleybus" />
      <p class="italic" style="margin-bottom: 1.5rem;">Le 27 octobre 1913, un tramway est sorti des voies à l'intersection de la rue du Valentin et de l'avenue Vinet, en raison d’une rupture des freins. Collection Daniel Corboz<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">38</sup></p>
      <img src="static/img/trolleybus1932.jpeg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Accident de tramway et premier trolleybus" />
      <p class="italic">Trolleybus en service (1939)<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">39</sup></p>
    </div>
  </div>
</div>

<div id="expo-1964" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">1964</div>
  <h2>L'Expo 64 : L'apothéose de l'automobile et la fin du tramway historique</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        L'année 1964 représente un moment de rupture identitaire pour Lausanne. En janvier, quelques mois seulement avant l'ouverture de l'Exposition nationale suisse (Expo 64), la dernière course du tram 7 (Renens - La Rosiaz) sonne le glas du réseau de tramways historiques.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">5</sup> Cette disparition est vécue comme un sacrifice nécessaire sur l'autel du progrès et de la modernité triomphante, symbolisée par l'automobile.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">1</sup>
      </p>
      <p>
        L'Expo 64 transforme Lausanne en une vitrine technologique mondiale. Pour acheminer les 12 millions de visiteurs, des infrastructures massives sont construites, notamment l'autoroute A1 entre Genève et Lausanne, qui s'achève au giratoire de la Maladière.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">9</sup> À l'intérieur du site de l'exposition, la mobilité devient elle-même une attraction :
      </p>
      <ul class="list-disc">
        <li><strong>Le Monorail Von Roll :</strong> Un système de transport futuriste qui survole les pavillons. Après l'événement, il sera démonté et réinstallé à Montréal pour l'Expo 67.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">9</sup></li>
        <li><strong>Le Télécanapé :</strong> Un moyen de transport par câble offrant une vue panoramique sur les rives du lac.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">10</sup></li>
        <li><strong>Le Mésoscaphe "Auguste Piccard" :</strong> Premier sous-marin touristique au monde, il permet à 33 000 personnes d'explore les fonds du Léman.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">9</sup></li>
      </ul>
      <p>
        Pendant que ces innovations captivent les foules, les TL renforcent leur réseau de bus et trolleybus pour pallier l'absence des trams. Cependant, l'héritage de 1964 est ambivalent : si l'aménagement des rives du lac et la création de parcs comme celui de Vidy sont des succès durables, la suppression totale du rail urbain de surface créera, quelques décennies plus tard, un vide capacitaire difficile à combler.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">9</sup>
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/meso-1964.jfif" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Le Mésoscaphe “Auguste Piccard” inauguré à l’Expo 64" />
      <p class="italic" style="margin-bottom: 1.5rem;">Le Mésoscaphe “Auguste Piccard” lors de l’Expo 64<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">44</sup></p>
      <img src="static/img/expo64.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Le Mésoscaphe et la Vallée de la Jeunesse" />
      <p class="italic">Le giratoire de la Maladière lors de l’Expo 64<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">45</sup></p>
    </div>
  </div>
</div>

<div id="m1-1991" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">1991</div>
  <h2>Genèse du campus EPFL-UNIL et l'avènement du métro M1 (TSOL)</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        Le déplacement des hautes écoles lausannoises vers Dorigny et Écublens dès 1968 marque la fin d'une ère agricole pour l'Ouest lausannois. Ce projet oppose deux visions : celle de l'UNIL (1972), conçue par Guido Cocchi comme un parc paysager décentralisé, et celle de l'EPFL (1969), pensée par Zweifel et Strickler comme une "mégastructure" modulaire et industrielle. Cet isolement géographique crée immédiatement une fracture avec le centre-ville, rendant les lignes de bus 18 et 19 rapidement obsolètes face à une population de 8 000 usagers dès 1985.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">28</sup>
      </p>
      <p>
        Pour désenclaver le campus, le Canton de Vaud retient en 1984 l'option d'un métro léger (TSOL), inspiré du Sneltram néerlandais. Les travaux débutent en 1988 pour un coût de 192 millions de francs suisses (dont 50 % financés par la Confédération). Inaugurée le 24 mai 1991, la ligne de 7,8 km relie Renens-Gare au Flon en 19 minutes. Techniquement, le m1 est un hybride : il circule majoritairement en surface avec des passages à niveau, mais emprunte un tunnel de 404 mètres au centre-ville et brave des rampes de 6%.
      </p>
      <p>
        Le succès du TSOL est immédiat : 7,4 millions de voyageurs la première année.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">13</sup> En 2000, le TSOL est officiellement intégré à la nomenclature des métros sous l'indice M1.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">2</sup> Malgré sa vitesse commerciale modeste (25 km/h) et ses nombreux passages à niveau, il devient indispensable à la vie académique lausannoise, transportant plus de 15 millions de passagers par an au début des années 2020.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">13</sup>
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/epfl-1991.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Conception EPFL et plan m1" />
      <p class="italic" style="margin-bottom: 1.5rem;">Conception de couleur du projet EPFL (1976) <sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">43</sup></p>
      <img src="static/img/m1-1991.svg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Conception EPFL et plan m1" />
      <p class="italic">Plan du m1<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">13</sup></p>
    </div>
  </div>
</div>

<div id="m2-2008" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">2008</div>
  <h2>La révolution du M2 : Un record mondial de verticalité</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        L'événement le plus transformateur de la mobilité contemporaine est sans conteste la mise en service du métro M2 le 27 octobre 2008.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">1</sup> Ce projet succède à la vénérable "Ficelle", dont l'exploitation s'arrête définitivement en janvier 2006 pour permettre sa métamorphose.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">2</sup> Le M2 n'est pas seulement un moyen de transport ; c'est un exploit d'ingénierie : le premier métro automatique de Suisse et le métro automatique présentant la plus forte pente au monde (12%).<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">1</sup>
      </p>
      <p>
        Le tracé de 5,95 km relie Ouchy au sud à Épalinges (Croisettes) au nord, traversant le cœur de la ville en souterrain. Les rames circulent sur pneumatiques pour garantir une adhérence maximale sur les rampes abruptes.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">2</sup> Le budget de 736 millions de francs suisses est respecté, financé à 60% par le canton de Vaud.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">1</sup>
      </p>
      <div class="overflow-x-auto mt-6 mb-6 rounded-lg border border-zinc-200 shadow-sm">
        <table class="w-full text-left bg-zinc-50 border-collapse">
          <thead>
            <tr class="bg-zinc-100 border-b border-zinc-300">
              <th class="py-3 px-4 font-bold text-zinc-900 text-sm md:text-base">Indicateur de performance du M2</th>
              <th class="py-3 px-4 font-bold text-zinc-900 text-sm md:text-base">Valeur</th>
            </tr>
          </thead>
          <tbody class="text-sm md:text-base text-zinc-700 font-medium">
            <tr class="border-b border-zinc-200"><td class="py-3 px-4">Longueur</td><td class="py-3 px-4">5,95 km</td></tr>
            <tr class="border-b border-zinc-200"><td class="py-3 px-4">Nombre de stations</td><td class="py-3 px-4">14</td></tr>
            <tr class="border-b border-zinc-200"><td class="py-3 px-4">Dénivelé total</td><td class="py-3 px-4">338 m</td></tr>
            <tr class="border-b border-zinc-200"><td class="py-3 px-4">Pente maximale</td><td class="py-3 px-4">12%</td></tr>
            <tr class="border-b border-zinc-200"><td class="py-3 px-4">Fréquence en pointe</td><td class="py-3 px-4">2 min 10 s</td></tr>
            <tr class="border-b border-zinc-200"><td class="py-3 px-4">Fréquentation annuelle (2019)</td><td class="py-3 px-4">32,8 millions <sup class="text-red-600 font-bold">15</sup></td></tr>
            <tr><td class="py-3 px-4">Prévision de fréquentation (2040)</td><td class="py-3 px-4">60 millions <sup class="text-red-600 font-bold">16</sup></td></tr>
          </tbody>
        </table>
      </div>
      <p>
        Le m2 a radicalement résolu la fracture topographique nord-sud de Lausanne en offrant une alternative performante à la saturation routière. Succédant à la « Ficelle », ce métro automatique a permis de relier Ouchy à Épalinges en seulement 18 minutes, surmontant un dénivelé de 338 mètres. Cette liaison directe a mis fin à l'isolement relatif du pôle hospitalier (CHUV, inauguré en 1983) et du secteur de l'innovation Biopôle (créé en 2004), désormais accessibles en quelques minutes depuis la gare CFF sans subir les aléas du trafic de surface.
      </p>
      <p>
        L'adoption du M2 par la population est massive. Alors que les prévisions tablaient sur 25 millions de passagers annuels à terme, ce chiffre est dépassé dès les premières années d'exploitation.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">1</sup> En 2019, la ligne transporte 32,8 millions de passagers, créant des situations de saturation chronique, notamment sur le tronçon Gare-Flon.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">4</sup>
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/m2-2008.svg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Plan et station M2" />
      <p class="italic" style="margin-bottom: 1.5rem;">Plan de la ligne du m2<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">2</sup></p>
      <img src="static/img/station-2008.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Plan et station M2" />
      <p class="italic">Station Lausanne-Gare<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">2</sup></p>
    </div>
  </div>
</div>

<div id="bus-ouest-2019" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">2019</div>
  <h2>Le défi de l'Ouest et l'essor du bus face au Pôle académique</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        La période 2000-2025 a transformé le réseau de bus lausannois en une véritable infrastructure de soutien à la métropolisation, avec un focus spectaculaire sur le Pôle académique d'Écublens (UNIL/EPFL). Face à la saturation critique du métro m1, qui a vu sa fréquentation doubler pour atteindre 15 millions de passagers annuels, les transports publics de la région lausannoise (tl) ont dû densifier massivement l'offre routière dans l'Ouest lausannois. Le déploiement de la ligne 31 (Renens-Gare – Venoge Sud) incarne cette mutation : d'une desserte secondaire, elle est devenue une des artères vitales du campus, reliant les nouveaux quartiers d'habitation comme le Vortex, inauguré en 2019 pour loger plus de 1000 étudiants, et le Parc scientifique.
      </p>
      <p>
        Selon les rapports de gestion des tl entre 2010 et 2024, le nombre de kilomètres parcourus par les bus dans le secteur Ouest a progressé de plus de 35 %, une hausse corrélée à l'installation de près de 35 000 étudiants et collaborateurs quotidiens sur le site.
      </p>
      <p>
        Cette densification s'appuie sur l'introduction, dès 2013, des bus à haute capacité (Hess lighTram) de 25 mètres, permettant d'offrir des fréquences à 7,5 minutes aux heures de pointe sur des axes auparavant sous-dotés. L’intégration du réseau de bus au projet d'agglomération Lausanne-Morges (PALM) a également permis de créer des sites propres (voies réservées), augmentant la vitesse commerciale de 15 % malgré l'engorgement du trafic privé.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">31</sup>
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/bus-ouest-2019.jpg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Ligne 31 et campus" />
      <p class="italic">Photographie d’un bus de la ligne 31, 2026</p>
    </div>
  </div>
</div>

<div id="vennes-2025" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">2025</div>
  <h2>Densification péri-centrale : L’essor des Fiches-Croisettes-Vennes</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        Le développement du secteur Les Fiches-Croisettes-Vennes incarne parfaitement la stratégie de densification « péri-centrale » de Lausanne, portée par l'arrivée du métro m2 en 2008. Ce plateau, autrefois peu bâti, a connu une mutation importante avec la création de l'éco-quartier des Fiches Nord, un projet d'envergure ayant accueilli environ 1 500 nouveaux résidants et des centaines d'emplois sur un site stratégiquement situé entre les stations Vennes et Croisettes à partir de 2016. Cette explosion démographique et l'essor simultané du Biopôle (parc scientifique dédié aux sciences de la vie créé en 2004) ont nécessité une restructuration profonde du réseau de bus pour assurer la capillarité autour de l'épine dorsale du métro.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">32</sup>
      </p>
      <p>
        La création et le renforcement des lignes 45 et 46 illustrent cette dynamique : la ligne 46 assure désormais une desserte fine de l'éco-quartier, reliant les nouvelles zones résidentielles aux interfaces de transport lourd, tandis que la ligne 45 joue un rôle de transversale cruciale en connectant les hauts d'Épalinges au terminus du métro à Croisettes. Selon le Schéma directeur de l'Est lausannois, ces lignes ont permis de stabiliser une part modale des transports publics supérieure à 40 % dans ce nouveau quartier.
      </p>
      <p>
        Le pôle de Vennes, avec son parking relais (P+R) de 1 200 places et l'aquarium-musée Aquatis, complète ce dispositif en faisant des lignes de bus locales le liant indispensable entre les flux autoroutiers, les zones de bureaux du Biopôle et les résidences des Fiches. Les chiffres de la stratégie « Horizon 2025 » des tl confirment cette trajectoire : l'offre globale a franchi le cap des 20 millions de kilomètres annuels, s'accompagnant d'une électrification totale de la flotte du campus.
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/biopole-2025.jpeg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Biopôle et éco-quartier" />
      <p class="italic" style="margin-bottom: 1.5rem;">Vues du Biopôle<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">40</sup></p>
      <img src="static/img/vennes-2025.jfif" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Biopôle et éco-quartier" />
      <p class="italic">Vues de l’éco-quartier des Fiches Nord<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">41</sup></p>
    </div>
  </div>
</div>

<div id="futur-2030" class="article-historique w-11/12 max-w-6xl mx-auto hidden pb-16 pt-10">
  <div class="text-red-600">2030</div>
  <h2>Vers 2030 : Le projet "Axes Forts", le Tram T1 et le Métro M3</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        Aujourd'hui, Lausanne est entrée dans une nouvelle phase d'expansion majeure avec pour objectif est de créer un réseau "d'axes forts" combinant métros, tramways et bus à haut niveau de service (BHNS).<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">4</sup>
      </p>
      <p>
        Le premier volet est le retour du tramway avec la ligne T1, reliant le Flon à la gare de Renens.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">18</sup> Le chantier a débuté symboliquement le 28 août 2021, soit exactement 125 ans après l'inauguration des premiers trams lausannois.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">18</sup> Cette ligne de 4,5 km, dotée de rames Stadler Tramlink de 45 mètres, devrait transporter 13 millions de voyageurs dès sa première année complète d'exploitation en 2027.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">18</sup>
      </p>
      <p>
        Le second volet est la création de la ligne de métro M3, qui reliera la gare de Lausanne à la Blécherette.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">22</sup> Ce projet nécessite une restructuration lourde du nœud de la gare. Le M3 utilisera le tunnel existant entre la Gare et le Flon, tandis qu'un nouveau tunnel à double voie sera percé pour le M2 afin d'augmenter sa cadence à 1 minute 30 secondes.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">23</sup> Le coût de ce programme de modernisation et d'extension est estimé à plus de 800 millions de francs suisses.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">14</sup>
      </p>
      <div class="overflow-x-auto mt-6 mb-6 rounded-lg border border-zinc-200 shadow-sm">
        <table class="w-full text-left bg-zinc-50 border-collapse">
          <thead>
            <tr class="bg-zinc-100 border-b border-zinc-300">
              <th class="py-3 px-4 font-bold text-zinc-900 text-sm md:text-base">Projet d'avenir</th>
              <th class="py-3 px-4 font-bold text-zinc-900 text-sm md:text-base">Mise en service</th>
              <th class="py-3 px-4 font-bold text-zinc-900 text-sm md:text-base">Capacité / Fréquence</th>
            </tr>
          </thead>
          <tbody class="text-sm md:text-base text-zinc-700 font-medium">
            <tr class="border-b border-zinc-200"><td class="py-3 px-4">Tramway T1</td><td class="py-3 px-4">Octobre 2026</td><td class="py-3 px-4">13 - 18 Mio voy./an</td></tr>
            <tr class="border-b border-zinc-200"><td class="py-3 px-4">Métro M3</td><td class="py-3 px-4">2034 - 2037</td><td class="py-3 px-4">40 Mio voy./an (2040)</td></tr>
            <tr><td class="py-3 px-4">Modernisation M2</td><td class="py-3 px-4">2030+</td><td class="py-3 px-4">Cadence 1'30''</td></tr>
          </tbody>
        </table>
      </div>
      <p>
        Le troisième volet concerne la mise en place de Bus à Haut Niveau de Service (BHNS). Ces "super bus" de grande capacité circulent sur des voies réservées avec priorité aux carrefours. Cette stratégie globale vise à accompagner une croissance démographique soutenue, le canton de Vaud prévoyant d'atteindre un million d'habitants d'ici 2044.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">4</sup>
      </p>
    </div>
    <div class="mt-12 md:mt-0 md:w-1/2">
      <img src="static/img/futur-2030.jpeg" class="w-full h-auto rounded-lg shadow-xl border border-zinc-200" alt="Plan du réseau 2030" />
      <p class="italic">Plan du réseau (hors bus) en 2030<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">42</sup></p>
    </div>
  </div>
</div>

</div>

  <div id="intro-texte" class="article-historique w-full md:w-11/12 mx-auto text-center pt-6 pb-2 text-zinc-500 italic">
  Cliquez sur un marqueur rouge sur la carte pour découvrir les étapes clés de la mobilité lausannoise.
</div>

<div class="tm-container py-4 text-white font-sans mt-2 w-full">
</div>

<div class="py-6"></div>

<div id="analyse-globale-permanente" class="article-historique w-11/12 max-w-6xl mx-auto pb-16 pt-10 border-t border-zinc-700">
  
  <h2 class="titre-evenement"> Analyse des dynamiques de fréquentation et perspectives de développement</h2>
  
  <div class="flex flex-col md:flex-row gap-8 lg:gap-12 items-start">
    <div class="md:w-1/2">
      <p>
        L'évolution de la fréquentation des transports publics lausannois témoigne d'une transformation profonde des habitudes de mobilité. Au début des années 2000, la gare de Lausanne accueillait environ 25 000 voyageurs quotidiens ; en 2019, ce chiffre est passé à 60 000, soit une hausse de 140%.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">4</sup> Cette accélération est directement corrélée à l'amélioration de l'offre de transport urbain.
      </p>
      <p>
        Le succès du M2 a agi comme une preuve de concept pour l'ensemble de l'agglomération. En 2008, la fréquentation annuelle du réseau TL était de 71,7 millions de voyageurs. En 2019, elle atteignait 120 millions.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">4</sup> Malgré l'interruption causée par la pandémie de Covid-19 en 2020, où la fréquentation du M2 a chuté de 31%, la reprise a été extrêmement rapide, dépassant les niveaux de 2019 dès 2023.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">15</sup>
      </p>
      <p>
        Cette saturation des infrastructures existantes impose des investissements massifs. Le projet de modernisation du M2 et de construction du M3, initialement chiffré à 1,1 milliard de francs en 2018, est désormais estimé à près de 2 milliards en incluant le renchérissement et les adaptations techniques complexes du sous-sol de la gare.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">26</sup> Ces montants, bien que considérables, sont jugés nécessaires pour éviter la paralysie d'une agglomération qui mise sur la densification vers l'intérieur pour préserver son paysage lémanique.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">19</sup>
      </p>
      <p>
        L'avenir des transports lausannois se dessine donc sous le signe de l'intermodalité et de la haute performance technologique. L'intégration progressive du LEB (Lausanne-Échallens-Bercher), qui circule désormais toutes les 15 minutes depuis 2020, et le développement du RER Vaud complètent ce dispositif.<sup class="text-sm md:text-base text-red-600 font-bold ml-0.5">16</sup> Lausanne, autrefois pionnière du tramway électrique et du trolleybus, s'impose aujourd'hui comme un modèle de "ville verticale" où la technologie ferroviaire la plus avancée est mise au service d'une urbanité durable et accessible.
      </p>
    </div>
  </div>
</div>

<a href="#top-of-page" id="back-to-top" class="fixed right-10 bottom-10 hidden z-50 bg-white rounded-full p-2 shadow-2xl">
  <svg width="40" height="40" viewBox="0 0 100 100">
    <path fill="black" d="m50 0c-13.262 0-25.98 5.2695-35.355 14.645s-14.645 22.094-14.645 35.355 5.2695 25.98 14.645 35.355 22.094 14.645 35.355 14.645 25.98-5.2695 35.355-14.645 14.645-22.094 14.645-35.355-5.2695-25.98-14.645-35.355-22.094-14.645-35.355-14.645zm20.832 62.5-20.832-22.457-20.625 22.457c-1.207 0.74219-2.7656 0.57812-3.7891-0.39844-1.0273-0.98047-1.2695-2.5273-0.58594-3.7695l22.918-25c0.60156-0.61328 1.4297-0.96094 2.2891-0.96094 0.86328 0 1.6914 0.34766 2.293 0.96094l22.918 25c0.88672 1.2891 0.6875 3.0352-0.47266 4.0898-1.1562 1.0508-2.9141 1.0859-4.1133 0.078125z"></path>
  </svg>
</a>

```js
(async () => {

  const yearSteps = [1907, 1925, 1937, 1973, 1983, 2000, 2025];

  // Mapping pour SwissTopo (années disponibles)
  const swissTopoYears = {
    1907: 19071231,
    1925: 19251231,
    1925: 19251231,
    1925: 19251231,
    1937: 19371231,
    1973: 19731231,
    1983: 19831231,
    2000: 20001231,
    2025: 20211231
  };

  const transportDefinitions = {
      1907: [
        {
          data: FileAttachment("data/trans_1907/1907_tram.geojson"),
          color: "#4a9d01",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          data: FileAttachment("data/trans_1907/1907_funiculaire.geojson"),
          color: "#ce00f8",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/trans_1907/1907_train.geojson"),
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/limits/1907_lim.geojson"),
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      1925: [
        {
          data: FileAttachment("data/trans_1925/1925_bus.geojson"),
          color: "#1f78b4",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          data: FileAttachment("data/trans_1925/1925_tram.geojson"),
          color: "#4a9d01",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          data: FileAttachment("data/trans_1925/1925_funiculaire.geojson"),
          color: "#ce00f8",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/trans_1925/1925_train.geojson"),
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/limits/1925_lim.geojson"),
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      1937: [
        {
          data: FileAttachment("data/trans_1937/1937_tram.geojson"),
          color: "#4a9d01",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          data: FileAttachment("data/trans_1937/1937_funiculaire.geojson"),
          color: "#ce00f8",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/trans_1937/1937_train.geojson"),
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/limits/1937_lim.geojson"),
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      1973: [
        {
          data: FileAttachment("data/trans_1973/1973_busv3.geojson"),
          color: "#1f78b4",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          data: FileAttachment("data/trans_1973/1973_funi.geojson"),
          color: "#ce00f8",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/trans_1973/1973_ferv2.geojson"),
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/limits/1973_lim.geojson"),
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      1983: [
        {
          data: FileAttachment("data/trans_1983/rout_ligne_v2.geojson"),
          color: "#1f78b4",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          data: FileAttachment("data/trans_1983/funiculaire.geojson"),
          color: "#ce00f8",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/trans_1983/ferroviaire_v2.geojson"),
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/limits/1983_lim.geojson"),
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      2000: [
        {
          data: FileAttachment("data/trans_2000/ROUTE_ligne_2000.geojson"),
          color: "#1f78b4",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          data: FileAttachment("data/trans_2000/FUNI_ligne_2000.geojson"),
          color: "#ce00f8",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/trans_2000/FER_ligne_2000.geojson"),
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          data: FileAttachment("data/limits/2000_lim.geojson"),
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      2025: [
        {
          data: FileAttachment("data/trans_2025/ROUTE_ligne_2025.geojson"),
          color: "#1f78b4",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          data: FileAttachment("data/trans_2025/FER_ligne_2025.geojson"),
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
      ],
    };

  const slider = document.getElementById("year-slider");
  const dateText = document.getElementById("date-text");
  const backToTop = document.getElementById("back-to-top");

    const map = L.map("map", {
      minZoom: 12,
      maxZoom: 16,
      maxBounds: [
        [46.45, 6.3],
        [46.7, 6.9],
      ],
      maxBoundsViscosity: 1,
    }).setView([46.519, 6.633], 13);

  map.createPane("transportPane");
  map.getPane("transportPane").style.zIndex = 450;

  const activeTransportLayers = L.layerGroup().addTo(map);

  // 🔹 Couche de base dynamique
  let baseLayer;

  function updateBaseMap(year) {
    if (baseLayer) {
      map.removeLayer(baseLayer);
    }

    const yearForMap = swissTopoYears[year] || year;

    const url = `https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.zeitreihen/default/${yearForMap}/3857/{z}/{x}/{y}.png`;

    baseLayer = L.tileLayer(url, {
      attribution: "© SwissTopo",
      tileSize: 256,
      opacity: 0.6
    });

    baseLayer.addTo(map);
  }

  async function loadLayer(definition) {
    const data = await definition.data.json();

    return L.geoJSON(data, {
      pane: "transportPane",
      style: {
        color: definition.color,
        weight: definition.weight,
        opacity: definition.opacity,
      },
    });
  }

  const transportLayersByYear = {};

  await Promise.all(
    yearSteps.map(async (year) => {
      const defs = transportDefinitions[year] ?? [];
      transportLayersByYear[year] = await Promise.all(defs.map(loadLayer));
    })
  );

  function showYear(year) {
    dateText.textContent = String(year);

    // 🔹 Update fond de carte
    updateBaseMap(year);

    // 🔹 Update transports
    activeTransportLayers.clearLayers();
    const layers = transportLayersByYear[year] ?? [];
    layers.forEach(layer => layer.addTo(activeTransportLayers));
  }

  slider.addEventListener("input", () => {
    const year = yearSteps[Number(slider.value)] ?? yearSteps[0];
    showYear(year);
  });

  // 🔹 Initialisation
  showYear(yearSteps[Number(slider.value)] ?? yearSteps[0]);

    // --- CRÉATION DE LA LÉGENDE LEAFLET ---
    const legend = L.control({ position: "topright" });

    legend.onAdd = function () {
    const div = L.DomUtil.create("div", "info legend-box");
    
    // Structure HTML interne de la légende blanche
    div.innerHTML = `
        <h4 class="legend-title">Types de transport</h4>
        <div class="legend-item"><span class="legend-line" style="background-color: #e31a1c"></span>Chemin de fer</div>
        <div class="legend-item"><span class="legend-line" style="background-color: #4a9d01"></span>Tramway</div>
        <div class="legend-item"><span class="legend-line" style="background-color: #1f78b4"></span>Bus / Trolleybus</div>
        <div class="legend-item"><span class="legend-line" style="background-color: #ce00f8"></span>Funiculaire</div>
    `;
    return div;
    };

    legend.addTo(map);

    const jalonIcon = L.icon({
      iconUrl: 'https://png.pngtree.com/png-vector/20250429/ourmid/pngtree-3d-red-map-marker-icon-for-accurate-location-pinpointing-png-image_16052221.png', 
      iconSize: [40, 40],
      iconAnchor: [20, 40], 
      popupAnchor: [0, -40],
    });

    // Vos données historiques extraites du texte
    const historiquesPinpoints = [
  {
    id: "leb-1873",
    coords: [46.532325, 6.611631], // Tunnel du LEB sous l’avenue d’Échallens
    titre: "Le chemin de fer LEB",
    annee: "1873",
    desc: "De la « Brouette » agricole à un véritable RER suburbain avec l'inauguration du nouveau tunnel.",
    img: await FileAttachment("static/img/leb-1873.jpg").url()
  },
  {
    id: "ficelle-1877",
    coords: [46.510983, 6.627750], // Funiculaire Lausanne-Ouchy
    titre: "L'émergence de la \"Ficelle\"",
    annee: "1877",
    desc: "Mise en service du funiculaire Lausanne-Ouchy, une prouesse technique majeure utilisant l'énergie hydraulique.",
    img: await FileAttachment("static/img/ficelle.jpg").url()
  },
  {
    id: "tramways-1896",
    coords: [46.524361, 6.636965], // Dépôt et centrale électrique
    titre: "La révolution électrique",
    annee: "1896",
    desc: "Inauguration du réseau de tramways électriques, un défi technique audacieux pour vaincre les fortes pentes.",
    img: await FileAttachment("static/img/tramways-1896.jpg").url()
  },
  {
    id: "signal-1899",
    coords: [46.529317, 6.639013], // Funiculaire Lausanne-Signal
    titre: "Funiculaire Lausanne-Signal",
    annee: "1899",
    desc: "Troisième infrastructure à câble de la ville, reliant le Vallon au belvédère du Signal pour le tourisme local.",
    img: await FileAttachment("static/img/affiche-1899.jpg").url()
  },
  {
    id: "bus-1920",
    coords: [46.525365, 6.635896], // Cœur historique (Cité)
    titre: "Les premières lignes de bus",
    annee: "1920",
    desc: "L'autobus devient un complément flexible pour desservir la colline escarpée de la Cité et les plages de l'Ouest.",
    img: await FileAttachment("static/img/bus-1920.jpg").url()
  },
  {
    id: "trolleybus-1932",
    coords: [46.524672, 6.631081], // Accident de tramway / transition
    titre: "Le tournant du Trolleybus",
    annee: "1932",
    desc: "Expérimentation du trolleybus offrant une meilleure adhérence, marquant le début du mouvement vers le « tout-pneu ».",
    img: await FileAttachment("static/img/trolleybus1932.jpeg").url()
  },
  {
    id: "expo-1964",
    coords: [46.517135, 6.603538], // Giratoire de la Maladière
    titre: "L'Expo 64 et l'automobile",
    annee: "1964",
    desc: "Fin des tramways historiques, triomphe de la voiture individuelle et vitrine de transports futuristes.",
    img: await FileAttachment("static/img/expo64.jpg").url()
  },
  {
    id: "m1-1991",
    coords: [46.521666, 6.571846], // Pôle universitaire
    titre: "L'avènement du métro M1",
    annee: "1991",
    desc: "Création du métro léger (TSOL) pour désenclaver les nouvelles hautes écoles de l'Ouest lausannois.",
    img: await FileAttachment("static/img/m1-1991.svg").url()
  },
  {
    id: "m2-2008",
    coords: [46.526183, 6.641558], // CHUV / M2
    titre: "La révolution du M2",
    annee: "2008",
    desc: "Le premier métro automatique de Suisse et le plus pentu au monde résout la fracture topographique nord-sud.",
    img: await FileAttachment("static/img/m2-2008.svg").url()
  },
  {
    id: "bus-ouest-2019",
    coords: [46.524500, 6.575296], // Vortex
    titre: "L'essor du bus à l'Ouest",
    annee: "2019",
    desc: "Densification massive de l'offre routière (bus à haute capacité) pour soutenir la croissance du Pôle académique.",
    img: await FileAttachment("static/img/bus-ouest-2019.jpg").url()
  },
  {
    id: "vennes-2025",
    coords: [46.542005, 6.662521], // Biopôle / Fiches Nord
    titre: "Densification péri-centrale",
    annee: "2025",
    desc: "Restructuration du réseau de bus autour du M2 pour accompagner l'essor de l'éco-quartier des Fiches et du Biopôle.",
    img: await FileAttachment("static/img/vennes-2025.jfif").url()
  },
  {
    id: "futur-2030",
    coords: [46.561196, 6.565426], // Croix-du-Péage (Terminus T1)
    titre: "Vers 2030 : T1 et M3",
    annee: "2030",
    desc: "L'avenir du réseau des axes forts avec le retour du tramway (T1), le nouveau métro M3 et les Bus à Haut Niveau de Service.",
    img: await FileAttachment("static/img/futur-2030.jpeg").url()
  }
];
    


    // Boucle pour créer tous les marqueurs sur la carte
    historiquesPinpoints.forEach(point => {
      const marker = L.marker(point.coords, { icon: jalonIcon }).addTo(map);
      
      const popupContent = `
        <div class="custom-popup">
          <div class="text-xs font-black text-white bg-red-600 inline-block px-2 py-1 rounded mb-2">${point.annee}</div>
          <h3 class="text-lg font-bold font-sans mt-0 leading-tight text-zinc-900">${point.titre}</h3>
          <p class="text-sm font-sans mb-1 text-zinc-700 mt-2">${point.desc}</p>
          <a href="#${point.id}" class="en-lire-plus text-sky-600 hover:text-sky-800 font-bold block mt-2 transition-colors">En lire plus</a>
          <img src="${point.img}" class="h-40 mx-auto block w-auto mt-3 rounded-sm border border-zinc-200" alt="${point.titre}" onerror="this.style.display='none'"/>
        </div>
      `;
      marker.bindPopup(popupContent, { minWidth: 260 });
    });

    function updateBackToTop() {
      const currentScrollY = window.scrollY || document.documentElement.scrollTop;
      if (backToTop) {
        backToTop.classList.toggle("hidden", currentScrollY < 200);
      }
    }

    window.addEventListener("scroll", updateBackToTop, { passive: true });
    if (backToTop) {
      backToTop.addEventListener("click", (event) => {
        event.preventDefault();
        window.scrollTo({ top: 0, behavior: "smooth" });
      });
    }

    document.addEventListener('click', function(e) {
      if (e.target && e.target.classList.contains('en-lire-plus')) {
        e.preventDefault();
        
        // 1. On récupère l'ID en enlevant le "#"
        const rawId = e.target.getAttribute('href').replace('#', '');
        console.log("🔘 Clic détecté ! Recherche de l'article avec l'ID exact : [" + rawId + "]");
        
        // 2. On cherche l'élément de manière sécurisée
        const targetElement = document.getElementById(rawId);
        
        if (targetElement) {
          console.log("✅ Article trouvé dans le HTML ! Défilement en cours...");
          
          // Cacher tous les autres articles historiques
          document.querySelectorAll('.article-historique').forEach(el => {
            el.classList.add('hidden');
          });

          // Afficher l'article ciblé
          targetElement.classList.remove('hidden'); 
          
          // Défiler doucement vers l'article
          const offsetTop = targetElement.getBoundingClientRect().top + window.scrollY - 50;
          window.scrollTo({ top: offsetTop, behavior: "smooth" });
          
        } else {
          // L'ERREUR S'AFFICHERA ICI SI LES NOMS NE CORRESPONDENT PAS
          console.error("❌ ERREUR : Impossible de trouver un <div id='" + rawId + "'> dans votre page HTML. Vérifiez l'orthographe !");
        }
      }
    });

    showYear(yearSteps[Number(slider.value)] ?? yearSteps[0]);
    updateBackToTop();
  })().catch((error) => {
    console.error(error);
  });
```
