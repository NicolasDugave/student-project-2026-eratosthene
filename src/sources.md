<style>
  /* --- COPIE DE LA SIDEBAR DE L'ACCUEIL --- */
  :root {
    --observablehq-max-width: 100% !important; 
  }
  html, body {
    overflow-x: hidden !important;
    overflow-y: auto !important;
    margin: 0 !important;
    padding: 0 !important;
    width: 100vw !important;
  }
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
  .observablehq-sidebar a, #observablehq-sidebar a {
    font-size: 1.2rem !important;
    font-weight: 500 !important;
  }
  .observablehq-main {
    width: 90vw !important;
    max-width: 90vw !important;
    margin-left: 10vw !important;
    padding: 2rem 4rem !important; /* Espacement confortable pour la lecture */
    box-sizing: border-box;
    min-height: 100vh !important;
  }

  /* --- STYLE DE L'ANALYSE HISTORIQUE --- */
  
  /* Style des dates pour les faire ressortir */
  .date-historique {
    font-family: 'Poppins', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    color: #e31a1c; /* Reprise du rouge de votre charte graphique */
    margin-top: 2rem;
    margin-bottom: 0.5rem;
    display: block;
    letter-spacing: -0.5px;
  }

  /* Justification et aération du texte */
  .analyse-texte p {
    text-align: justify;
    text-justify: inter-word;
    line-height: 1.7;
    margin-bottom: 1.2rem; /* Petit espace vide entre les paragraphes */
    color: #e4e4e7; /* Zinc-200 pour une lecture douce sur fond sombre */
    font-size: 1.1rem;
  }

  /* Disposition en colonnes (Texte à gauche / Images à droite) */
  .section-historique {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    margin-bottom: 4rem;
  }

  @media (min-width: 768px) {
    .section-historique {
      flex-direction: row;
      align-items: flex-start;
    }
    .analyse-texte {
      width: 60%; /* Le texte prend 60% de la largeur */
    }
    .analyse-images {
      width: 40%; /* La colonne d'images prend 40% */
      display: flex;
      flex-direction: column;
      align-items: flex-end; /* Aligne les images contre le bord droit */
      gap: 1.5rem; /* Espace entre les images si vous en avez plusieurs */
    }
  }

  /* Style de base des images pour éviter les débordements */
  .analyse-images img {
    max-width: 100%;
    height: auto;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  }
</style>

<!-- ========================================== -->
<!-- SECTION SOURCES ET BIBLIOGRAPHIE           -->
<!-- ========================================== -->
<div id="sources-bibliographie" class="w-11/12 max-w-6xl mx-auto pt-20 pb-24">
  
  <h2 class="text-3xl md:text-4xl font-black italic mb-8 text-zinc-900 border-b-4 border-red-600 pb-3 inline-block">
    Sources et Bibliographie
  </h2>
  
  <div class="bg-zinc-50 p-6 md:p-10 rounded-2xl border border-zinc-200 shadow-sm">
    <ol class="space-y-10 text-sm md:text-base font-medium text-zinc-600 leading-relaxed list-disc pl-5 marker:text-red-600">
      <li>
        <span class="text-zinc-900">Le métro m2 à Lausanne : quelles nouvelles interfaces avec la ville et le canton? - Unil, consulté le avril 25, 2026</span>
        <a href="https://www.unil.ch/files/live/sites/ouvdd/files/shared/URBIA/urbia_13/articles/4._Le_metro_M2_a_Lausanne-_C._Jemelin__49-62.pdf" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.unil.ch/files/live/sites/ouvdd/files/shared/URBIA/urbia_13/articles/4._Le_metro_M2_a_Lausanne-_C._Jemelin__49-62.pdf</a>
      </li>
      <li>
        <span class="text-zinc-900">Ligne M2 du métro de Lausanne — Wikipédia, consulté le avril 25, 2026</span>
        <a href="https://fr.wikipedia.org/wiki/Ligne_M2_du_m%C3%A9tro_de_Lausanne" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://fr.wikipedia.org/wiki/Ligne_M2_du_métro_de_Lausanne</a>
      </li>
      <li>
        <span class="text-zinc-900">Transports publics de la région lausannoise — Wikipédia, consulté le avril 25, 2026</span>
        <a href="https://fr.wikipedia.org/wiki/Transports_publics_de_la_r%C3%A9gion_lausannoise" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://fr.wikipedia.org/wiki/Transports_publics_de_la_région_lausannoise</a>
      </li>
      <li>
        <span class="text-zinc-900">/// Développement des métros m2-m3 ///, consulté le avril 25, 2026</span>
        <a href="https://8008.ch/wp-content/uploads/Brochure-information-metros-m2-m3.pdf" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://8008.ch/wp-content/uploads/Brochure-information-metros-m2-m3.pdf</a>
      </li>
      <li>
        <span class="text-zinc-900">Le Tramway lausannois, acteur d'une histoire unique, consulté le avril 25, 2026</span>
        <a href="https://tramway-lausannois.ch/acteur-dune-histoire/" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://tramway-lausannois.ch/acteur-dune-histoire/</a>
      </li>
      <li>
        <span class="text-zinc-900">Ancien tramway de Lausanne — Wikipédia, consulté le avril 25, 2026</span>
        <a href="https://fr.wikipedia.org/wiki/Ancien_tramway_de_Lausanne" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://fr.wikipedia.org/wiki/Ancien_tramway_de_Lausanne</a>
      </li>
      <li>
        <span class="text-zinc-900">Il y a 50 ans, la fin du tram à Lausanne | Espazium, consulté le avril 25, 2026</span>
        <a href="https://www.espazium.ch/fr/actualites/il-y-50-ans-la-fin-du-tram-lausanne" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.espazium.ch/fr/actualites/il-y-50-ans-la-fin-du-tram-lausanne</a>
      </li>
      <li>
        <span class="text-zinc-900">Trams in Lausanne - Wikipedia, consulté le avril 25, 2026</span>
        <a href="https://en.wikipedia.org/wiki/Trams_in_Lausanne" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://en.wikipedia.org/wiki/Trams_in_Lausanne</a>
      </li>
      <li>
        <span class="text-zinc-900">Que reste-t-il de l'Exposition nationale suisse de 1964? - SWI swissinfo.ch, consulté le avril 25, 2026</span>
        <a href="https://www.swissinfo.ch/fre/cinquieme-suisse/que-reste-t-il-de-lexposition-nationale-suisse-de-1964/87780951" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.swissinfo.ch/fre/cinquieme-suisse/que-reste-t-il-de-lexposition-nationale-suisse-de-1964/87780951</a>
      </li>
      <li>
        <span class="text-zinc-900">Exposition nationale suisse de 1964 - Wikipédia, consulté le avril 25, 2026</span>
        <a href="https://fr.wikipedia.org/wiki/Exposition_nationale_suisse_de_1964" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://fr.wikipedia.org/wiki/Exposition_nationale_suisse_de_1964</a>
      </li>
      <li>
        <span class="text-zinc-900">Expo 64 – Le monorail - notreHistoire.ch, consulté le avril 25, 2026</span>
        <a href="https://notrehistoire.ch/documents/01k81d2cjm0s9kns1hqtfwntxz" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://notrehistoire.ch/documents/01k81d2cjm0s9kns1hqtfwntxz</a>
      </li>
      <li>
        <span class="text-zinc-900">Sur les traces de l'Expo 64 | Largeur.com, consulté le avril 25, 2026</span>
        <a href="https://largeur.com/?p=11115" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://largeur.com/?p=11115</a>
      </li>
      <li>
        <span class="text-zinc-900">Ligne M1 du métro de Lausanne — Wikipédia, consulté le avril 25, 2026</span>
        <a href="https://fr.wikipedia.org/wiki/Ligne_M1_du_m%C3%A9tro_de_Lausanne" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://fr.wikipedia.org/wiki/Ligne_M1_du_métro_de_Lausanne</a>
      </li>
      <li>
        <span class="text-zinc-900">Une enveloppe de 809 millions sollicitée pour les métros M2 et M3 à Lausanne | RTS, consulté le avril 25, 2026</span>
        <a href="https://www.rts.ch/info/regions/vaud/2025/article/lausanne-809-millions-pour-moderniser-les-metros-m2-et-m3-d-ici-2036-29073333.html" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.rts.ch/info/regions/vaud/2025/article/lausanne-809-millions-pour-moderniser-les-metros-m2-et-m3-d-ici-2036-29073333.html</a>
      </li>
      <li>
        <span class="text-zinc-900">ExMot Texte adopté par CE - EMPD3 Métros V03.00 - Canton de Vaud, consulté le avril 25, 2026</span>
        <a href="https://www.vd.ch/fileadmin/user_upload/accueil/fichiers_pdf/EMPD-EMPL/EMPD_21_LEG_175_financement_m2_m3.pdf" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.vd.ch/fileadmin/user_upload/accueil/fichiers_pdf/EMPD-EMPL/EMPD_21_LEG_175_financement_m2_m3.pdf</a>
      </li>
      <li>
        <span class="text-zinc-900">Métros m2 et m3 : Octroi de deux cautionnements aux tl Préavis Nº 2025 / 41 Lausanne, le 20 novembre 2025 Monsieur le Prés - Canton de Vaud, consulté le avril 25, 2026</span>
        <a href="https://www.vd.ch/fileadmin/user_upload/accueil/fichiers_pdf/2025_novembre_actus/1128-metros_m2_-_Pr%C3%A9avis_Ville_de_Lausanne.pdf" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.vd.ch/fileadmin/user_upload/accueil/fichiers_pdf/2025_novembre_actus/1128-metros_m2_-_Préavis_Ville_de_Lausanne.pdf</a>
      </li>
      <li>
        <span class="text-zinc-900">Métros m2 et m3 – Ville de Lausanne, consulté le avril 25, 2026</span>
        <a href="https://www.lausanne.ch/officiel/grands-projets/pole-gare/metros-m2-et-m3.html" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.lausanne.ch/officiel/grands-projets/pole-gare/metros-m2-et-m3.html</a>
      </li>
      <li>
        <span class="text-zinc-900">Tramway de Lausanne - Wikipédia, consulté le avril 25, 2026</span>
        <a href="https://fr.wikipedia.org/wiki/Tramway_de_Lausanne" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://fr.wikipedia.org/wiki/Tramway_de_Lausanne</a>
      </li>
      <li>
        <span class="text-zinc-900">Travaux Services industriels Axes forts de transports publics urbains (AFTPU) Projet de tramway entre la gare de Renens et la place de l'Europe - Ville de Lausanne, consulté le avril 25, 2026</span>
        <a href="https://www.lausanne.ch/apps/actualites/Next/serve.php?id=6200" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.lausanne.ch/apps/actualites/Next/serve.php?id=6200</a>
      </li>
      <li>
        <span class="text-zinc-900">125 ans traversés en commun - Transports publics Lausannois, consulté le avril 25, 2026</span>
        <a href="https://rapportannuel.t-l.ch/125-ans-traverses-en-commun/" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://rapportannuel.t-l.ch/125-ans-traverses-en-commun/</a>
      </li>
      <li>
        <span class="text-zinc-900">Lausanne tramway - Wikipedia, consulté le avril 25, 2026</span>
        <a href="https://en.wikipedia.org/wiki/Lausanne_tramway" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://en.wikipedia.org/wiki/Lausanne_tramway</a>
      </li>
      <li>
        <span class="text-zinc-900">Ligne M3 du métro de Lausanne - Wikipédia, consulté le avril 25, 2026</span>
        <a href="https://fr.wikipedia.org/wiki/Ligne_M3_du_m%C3%A9tro_de_Lausanne" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://fr.wikipedia.org/wiki/Ligne_M3_du_métro_de_Lausanne</a>
      </li>
      <li>
        <span class="text-zinc-900">Métros | État de Vaud, consulté le avril 25, 2026</span>
        <a href="https://www.vd.ch/mobilite/loffre-de-mobilite-a-votre-disposition/metros" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.vd.ch/mobilite/loffre-de-mobilite-a-votre-disposition/metros</a>
      </li>
      <li>
        <span class="text-zinc-900">ExMot EMPD m2-m3 2025_V02.00 - Canton de Vaud, consulté le avril 25, 2026</span>
        <a href="https://www.vd.ch/fileadmin/user_upload/accueil/fichiers_pdf/2025_novembre_actus/EMPD_m2-m3_2025.pdf" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.vd.ch/fileadmin/user_upload/accueil/fichiers_pdf/2025_novembre_actus/EMPD_m2-m3_2025.pdf</a>
      </li>
      <li>
        <span class="text-zinc-900">Transports publics lausannois : 133 millions de voyageurs en 2025 - La Télé, consulté le avril 25, 2026</span>
        <a href="https://latele.ch/articles/transports-publics-lausannois-frequentation-en-hausse-en-2025" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://latele.ch/articles/transports-publics-lausannois-frequentation-en-hausse-en-2025</a>
      </li>
      <li>
        <span class="text-zinc-900">Le M3, les dessous d'un chantier lausannois - citrap-vaud.ch, consulté le avril 25, 2026</span>
        <a href="https://www.citrap-vaud.ch/wp-content/uploads/2025/03/LT27.3.25.pdf" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.citrap-vaud.ch/wp-content/uploads/2025/03/LT27.3.25.pdf</a>
      </li>
      <li>
        <span class="text-zinc-900">Projet d'agglomération - Lausanne-Morges (PALM), consulté le avril 25, 2026</span>
        <a href="https://lausanne-morges.ch/wp-content/uploads/2019/11/palm_rapport_final_071219-1.pdf" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://lausanne-morges.ch/wp-content/uploads/2019/11/palm_rapport_final_071219-1.pdf</a>
      </li>
      <li>
        <span class="text-zinc-900">EPFL - Histoire du campus, consulté le 29 avril 2025</span>
        <a href="https://www.epfl.ch/about/overview/fr/histoire/" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.epfl.ch/about/overview/fr/histoire/</a>
      </li>
      <li>
        <span class="text-zinc-900">Les Tramways Lausannois 1896-1964, Grandguillaume et al.</span>
      </li>
      <li>
        <span class="text-zinc-900">État de Vaud. (2017, 21 août). Les travaux de construction du tunnel du LEB sous l’avenue d’Échallens vont commencer. consulté le 29 avril 2026</span>
        <a href="https://www.vd.ch/actualites/actualite/news/9445i-les-travaux-de-construction-du-tunnel-du-leb-sous-lavenue-dechallens-vont-commencer" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.vd.ch/actualites/actualite/news/9445i-les-travaux-de-construction-du-tunnel-du-leb-sous-lavenue-dechallens-vont-commencer</a>
      </li>
      <li>
        <span class="text-zinc-900">Projet d’agglomération Lausanne-Morges, consulté le 29 avril 2026</span>
        <a href="https://lausanne-morges.ch/rapports/rapport-2025/" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://lausanne-morges.ch/rapports/rapport-2025/</a>
      </li>
      <li>
        <span class="text-zinc-900">Plan Directeur Communal de Lausanne, 2022</span>
        <a href="https://www.lausanne.ch/officiel/grands-projets/lausanne-2030/plan-directeur-pdcom.html" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.lausanne.ch/officiel/grands-projets/lausanne-2030/plan-directeur-pdcom.html</a>
      </li>
      <li>
        <span class="text-zinc-900">Collection Martine Desarzens, profil et documents d'archives sur la fondation pour la sauvegarde du patrimoine audiovisuel de la RTS, consulté le 30 avril 2026</span>
        <a href="https://notrehistoire.ch/@zizou" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://notrehistoire.ch/@zizou</a>
      </li>
      <li>
        <span class="text-zinc-900">24 HEURES, Un siècle et demi de cohabitation difficile prendra fin ce vendredi , 12 mai 2022, consulté le 30 avril 2026</span>
        <a href="https://www.24heures.ch/un-siecle-et-demi-de-cohabitation-difficile-prendra-fin-ce-vendredi-514546078792" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.24heures.ch/un-siecle-et-demi-de-cohabitation-difficile-prendra-fin-ce-vendredi-514546078792</a>
      </li>
      <li>
        <span class="text-zinc-900">RTS, Plus de 2000 personnes ont inauguré le nouveau tunnel du LEB à Lausanne, 14 mai 2022, consulté le 30 avril 2026</span>
        <a href="https://www.rts.ch/info/regions/vaud/13093890-plus-de-2000-personnes-ont-inaugure-le-nouveau-tunnel-du-leb-a-lausanne.html" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.rts.ch/info/regions/vaud/13093890-plus-de-2000-personnes-ont-inaugure-le-nouveau-tunnel-du-leb-a-lausanne.html</a>
      </li>
      <li>
        <span class="text-zinc-900">Tramway Lausannois, Acteur d’une histoire, Association historique des trams lausannois, consulté le 30 avril 2026</span>
        <a href="https://tramway-lausannois.ch/acteur-dune-histoire/" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://tramway-lausannois.ch/acteur-dune-histoire/</a>
      </li>
      <li>
        <span class="text-zinc-900">24 HEURES, Histoire d'ici: 1948, Lausanne dit adieu au funiculaire du Signal, 31 octobre 2021, consulté le 30 avril 2026</span>
        <a href="https://www.24heures.ch/histoire-d-ici-1948-lausanne-dit-adieu-au-funiculaire-du-signal-249713694161" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.24heures.ch/histoire-d-ici-1948-lausanne-dit-adieu-au-funiculaire-du-signal-249713694161</a>
      </li>
      <li>
        <span class="text-zinc-900">Collection Daniel Corboz, profil et documents d'archives sur la fondation pour la sauvegarde du patrimoine audiovisuel de la RTS, consulté le 30 avril 2026</span>
        <a href="https://notrehistoire.ch/documents/01k81a609eqwxfw24amv4xfn7e" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://notrehistoire.ch/documents/01k81a609eqwxfw24amv4xfn7e</a>
      </li>
      <li>
        <span class="text-zinc-900">LFM, L'année où le trolley a détrôné le tram à Lausanne sur LFM.ch, consulté le 30 avril 2026</span>
        <a href="https://www.lfm.ch/loisirs/notrehistoire/lannee-ou-le-trolley-a-detrone-le-tram-a-lausanne/" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.lfm.ch/loisirs/notrehistoire/lannee-ou-le-trolley-a-detrone-le-tram-a-lausanne/</a>
      </li>
      <li>
        <span class="text-zinc-900">Article « Biopôle » sur Wikipédia, l'encyclopédie libre, consulté le 30 avril 2026</span>
        <a href="https://fr.wikipedia.org/wiki/Biop%C3%B4le" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://fr.wikipedia.org/wiki/Biopôle</a>
      </li>
      <li>
        <span class="text-zinc-900">Distinction Romande d’Architecture (DRA IV), fiche du projet « Les Fiches Nord, Lausanne », consulté le 30 avril 2026</span>
        <a href="https://dra5.ch/dra4/projets/1819/les-fiches-nord-lausanne/" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://dra5.ch/dra4/projets/1819/les-fiches-nord-lausanne/</a>
      </li>
      <li>
        <span class="text-zinc-900">Chantiers Magazine, Tramway Lausanne-Renens : un chantier d'envergure pour la mobilité de demain, consulté le 30 avril 2026</span>
        <a href="https://www.chantiersmagazine.ch/tramway-lausanne-renens/" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.chantiersmagazine.ch/tramway-lausanne-renens/</a>
      </li>
      <li>
        <span class="text-zinc-900">Zweifer & al., “Conception de couleur extérieure”, Conception du projet EPFL, vol.1, 1976</span>
      </li>
      <li>
        <span class="text-zinc-900">Archives de la RTS, La fantastique épopée du mésoscaphe sur rts.ch, consulté le 30 avril 2026</span>
        <a href="https://www.rts.ch/archives/9722848-la-fantastique-epopee-du-mesoscaphe.html#chap01" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.rts.ch/archives/9722848-la-fantastique-epopee-du-mesoscaphe.html#chap01</a>
      </li>
      <li>
        <span class="text-zinc-900">24 Heures, Lausanne: L’exposition nationale secoue la Suisse de 1964 sur 24heures.ch, consulté le 30 avril 2026</span>
        <a href="https://www.24heures.ch/lausanne-lexposition-nationale-secoue-la-suisse-de-1964-135028422209" target="_blank" class="block text-sky-600 hover:text-sky-800 transition-colors break-all mt-0.5">https://www.24heures.ch/lausanne-lexposition-nationale-secoue-la-suisse-de-1964-135028422209</a>
      </li>
    </ol>

  <h3>Sources cartographiques</h3>
<ol start="46">
  <li>Cartes transports 1907, 1973, 1983 et 2000 : Archives des Transports publics de la région lausannoise SA</li>
  <li>Carte transports ca. 1925 : Bibliothèque nationale de France (BnF), Lausanne-Ouchy Plage, Société des Transports de Lausanne, consulté le 19 mai 2026, <a href="https://catalogue.bnf.fr/ark:/12148/cb40695153f" target="_blank" rel="noopener noreferrer">https://catalogue.bnf.fr/ark:/12148/cb40695153f</a></li>
  <li>Carte transports 1937 : Archives de la Direction Générale de la Mobilité et des Routes</li>
  <li>Carte transports 2025 : ASIT (Association pour le système d'information du territoire), Carte des transports publics (Géodonnées et plans du réseau) sur le portail de référence <a href="https://viageo.ch" target="_blank" rel="noopener noreferrer">Viageo.ch</a></li>
  <li>Fonds de cartes : Office fédéral de topographie (swisstopo), Cartes historiques du territoire suisse (Séries temporelles) sur le portail <a href="https://geo.admin.ch" target="_blank" rel="noopener noreferrer">geo.admin.ch</a>, consulté le 19 mai 2026.</li>
</ol>
  </div>
</div>
