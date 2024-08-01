# activity_alert
WIP un sytème d'alerte pour se forcer à bouger de sa chaise à intervalle régulier

L'idée:
    un picopi
    une matrice 8x8
    un/des boutons
    un on/off?

[on/off][ SNOOOOOOZE ][reset]

fonctionnement
    On programme une durée par appui sur un bouton.
        délai initial 2h 
    A l'expiration du délai , la platine s'allume et provoque une gêne
        possibilité de retarder de 5 minutes en appuyant sur le bouton
        relance d'un nouveau délai de 2 heures
    
améliorations
    détection de présence et envoi d'un windows+l en cas d'absence.

    J'ai un picopi, une matrice de 8x8 leds ws2812b, et trois boutons (onoff snooze reset)
le bouton reset éteint les leds, et lance un timer de 2h.
le bouton snooze relance le timer pour 5 minutes.
le bouton onoff met tout le système en pause: extinction des leds, pause des timers.
quand le timer vient à expiration, la matrice de led lance une animation colorée qui dure maximun une minute. après quoi les leds sont éteintes et le timer est relance pour 5 minutes.
Si le bouton snooze est appuyé pendant l'animation, les leds sont éteintes et le timer relancé pour 5 minutes.
