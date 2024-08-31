# activity_alert
WIP un sytème d'alerte pour se forcer à bouger de sa chaise à intervalle régulier

L'idée:
    un picopi
    une matrice 8x8
    un/des boutons
    un on/off?

trois boutons:
[on/off][ SNOOZE ][reset]

on/off met le picopi en veille profonde/ le réactive
snooze - éteint la platine et relance le timer pour 5 minutes
reset - relance pour 2h

fonctionnement
    On programme un délai initial de 2h par appui sur un bouton.
         
    A l'expiration du délai , la platine s'allume et provoque une gêne visuelle
       - a l'appui sur snooze, extinction du panneau et relance de 5 minutes
       - a l'appui sur reset, extinction du panneau et relance d'un nouveau délai de 2 heures
       - si il n'y a pas d'action au bout d'une minute, passage en off



améliorations
    détection de présence et envoi d'un windows+l en cas d'absence.

    J'ai un picopi, une matrice de 8x8 leds ws2812b, et trois boutons (onoff snooze reset)
le bouton reset éteint les leds, et lance un timer de 2h.
le bouton snooze relance le timer pour 5 minutes.
le bouton onoff met tout le système en pause: extinction des leds, pause des timers.
quand le timer vient à expiration, la matrice de led lance une animation colorée qui dure maximun une minute. après quoi les leds sont éteintes et le timer est relance pour 5 minutes.
Si le bouton snooze est appuyé pendant l'animation, les leds sont éteintes et le timer relancé pour 5 minutes.
écrit moi le code circuitpython nécessaire pour obtenir cela. Merci.
