# Objectif
L'objectif de ce projet est de mesurer la performance d'un alogorithme de matching simple basée sur SIFT.

### La méthode utilisée et l'étude de cas en bref
 * On reçoit un couple d'images représenant deux étiquettes de vins.
 * On veut savoir s'il s'agit du même vin ou pas.
 * Pour chacune des images, on extrait les keypoints discriminants.
 * Via un KNN, on match les keypoints les plus proches
 * Si les deux images représentent l'étiquette d'un même vin alors leur nombre de keypoints matched doit être élevée.
 * Au contraire, si les deux images représentent l'étiquette de vins différents, alors on s'attend à observer un nombre de keypoints matched faible.

### Résumé des Résultats
* Si deux images représentent un même vin, alors le nombre de keypoints matched est relativement élevée. Ce nombre est d'autant plus grand que la qualité d'image est élevée.
* Si deux images représentent deux vins différents (différents producteurs), alors le nombre de keypoints est faible (<20) et ce quelque soit la qualité des images.
* Si deux images représentent des vins différents mais appartenant à un même producteur, alors le nombre de keypoints matched est relativement élevée. Cela est probablement dû à une charte graphique identique.