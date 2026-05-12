def calculer_taux_de_conversion(campagne):
   taux_de_conversion = campagne['visiteurs'] / campagne['conversions']
   return taux_de_conversion
taux_de_conversion1 = calculer_taux_de_conversion(premiere_campagne)
taux_de_conversion2 = calculer_taux_de_conversion(seconde_campagne)
taux_de_conversion3 = calculer_taux_de_conversion(troisieme_campagne)