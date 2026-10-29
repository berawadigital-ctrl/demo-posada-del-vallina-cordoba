# Contenido de la demo Hotel Hacienda Posada de Vallina (Cordoba) (es/ca/en/fr). Hechos de hhposadadevallina.es leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble y Twin','Doble económica y Doble con vistas','Doble con supletoria'],'ca':['Doble i Twin','Doble econòmica i Doble amb vistes','Doble amb llit supletori'],'en':['Double and Twin','Economy double and Double with views','Double with extra bed'],'fr':['Double et Twin','Double économique et Double avec vue','Double avec lit d\'appoint']}
RD={
'es':['Con cama de matrimonio o dos camas, aire acondicionado, wifi gratuito, TV LCD y minibar; baño privado con ducha y secador.','La económica, en planta baja junto al patio cordobés, con artesonado de madera; la de vistas, en la segunda planta, con balcón desde el que se ve la Mezquita.','Con tres camas, para viajar en familia o en grupo, con el mismo equipamiento que el resto de habitaciones.'],
'ca':['Amb llit de matrimoni o dos llits, aire condicionat, wifi gratuït, TV LCD i minibar; bany privat amb dutxa i assecador.','L\'econòmica, a la planta baixa al costat del pati cordovès, amb enteixinat de fusta; la de vistes, a la segona planta, amb balcó des d\'on es veu la Mesquita.','Amb tres llits, per viatjar en família o en grup, amb el mateix equipament que la resta d\'habitacions.'],
'en':['With a double bed or two beds, air conditioning, free wifi, LCD TV and minibar; private bathroom with shower and hairdryer.','The economy room, on the ground floor by the Cordoban patio, with a wooden coffered ceiling; the one with views, on the second floor, with a balcony overlooking the Mezquita.','With three beds, for families or groups, with the same equipment as the other rooms.'],
'fr':['Avec lit double ou deux lits, climatisation, wifi gratuit, TV LCD et minibar ; salle de bain privée avec douche et sèche-cheveux.','L\'économique, au rez-de-chaussée près du patio cordouan, avec plafond à caissons en bois ; celle avec vue, au deuxième étage, avec balcon donnant sur la Mezquita.','Avec trois lits, pour les familles ou les groupes, avec le même équipement que les autres chambres.']}
ART={
'hero':('arches',9701,['#f2e8d8','#e8bd8c','#b0532d','#73301a','#47200f']),
'intro':('columns',9702,['#efebe2','#f8f5ef','#b1582f','#73301a','#47200f']),
'r1':('arches',9711,['#f0e5d2','#e2b27e','#a74d2a','#73301a','#47200f']),
'r2':('skyline',9712,['#73301a','#e6a467','#f5d4a1','#2c4a3e','#233e33','#162a22']),
'r3':('hills',9713,['#e6ece5','#f1e9d3','#ecbb78','#a7bd9d','#7b9a81','#52735c']),
'g1':('columns',9721,['#edeae2','#f7f4ee','#ad5430','#73301a','#47200f']),
'g2':('arches',9722,['#eee2ce','#dfae79','#a24825','#73301a','#47200f']),
'g3':('skyline',9723,['#73301a','#e3a165','#f4d29e','#2a483c','#213b31','#152820']),
'g4':('hills',9724,['#e3eae2','#eee6ce','#eab875','#a4ba9a','#78977e','#4f7059']),
'g5':('waves',9725,['#2c4a3e','#edbd82','#f6deb5','#3c6657','#2c4a3e','#1a3028']),
'g6':('arches',9726,['#ecdfca','#dcab75','#9f4522','#73301a','#47200f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Hacienda Posada de Vallina · Junto a la Mezquita de Córdoba',see_rooms='Ver habitaciones',hero_k='Córdoba · Judería',hero_t='Una posada histórica junto a la Mezquita',hero_s='En el corazón de la Córdoba monumental, a 1 minuto a pie de la Mezquita-Catedral.',
 intro_t='Tradición y confort',intro_p1='Una posada con una historia que se remonta a la época de los Alarifes, en el barrio de la Judería, con patio cordobés.',
 intro_p2='Recepción 24 horas, wifi gratuito, bar, salón de uso compartido con zona de TV, biblioteca y ascensor.',
 stats=['5 tipos de habitación','Mezquita a 1 min','Recepción 24 h','Wifi gratuito'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Doble, Twin, Doble económica, Doble con vistas y Doble con supletoria, todas con aire acondicionado y baño privado.',
 svcs=['Recepción 24 horas','Wifi gratuito','Bar','Salón compartido y zona de TV','Biblioteca','Ascensor','Adaptado para movilidad reducida','Servicio de habitaciones 24 h'],
 loc_p='Corregidor Luis de la Cerda, 83 · 14003 Córdoba. Mezquita-Catedral a 1 minuto, Puente Romano a 5 y Alcázar a 7 minutos a pie.',
 chips=['¿Qué habitaciones tiene?','¿Dónde está?','¿Qué servicios tiene?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Hacienda Posada de Vallina · Al costat de la Mesquita de Còrdova',see_rooms='Veure habitacions',hero_k='Còrdova · Jueria',hero_t='Una posada històrica al costat de la Mesquita',hero_s='Al cor de la Còrdova monumental, a 1 minut a peu de la Mesquita-Catedral.',
 intro_t='Tradició i confort',intro_p1='Una posada amb una història que es remunta a l\'època dels Alarifes, al barri de la Jueria, amb pati cordovès.',
 intro_p2='Recepció 24 hores, wifi gratuït, bar, saló d\'ús compartit amb zona de TV, biblioteca i ascensor.',
 stats=['5 tipus d\'habitació','Mesquita a 1 min','Recepció 24 h','Wifi gratuït'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Doble, Twin, Doble econòmica, Doble amb vistes i Doble amb llit supletori, totes amb aire condicionat i bany privat.',
 svcs=['Recepció 24 hores','Wifi gratuït','Bar','Saló compartit i zona de TV','Biblioteca','Ascensor','Adaptat per a mobilitat reduïda','Servei d\'habitacions 24 h'],
 loc_p='Corregidor Luis de la Cerda, 83 · 14003 Còrdova. Mesquita-Catedral a 1 minut, Pont Romà a 5 i Alcàsser a 7 minuts a peu.',
 chips=['Quines habitacions té?','On és?','Quins serveis té?','Com es reserva?']),
'en':dict(title='Hotel Hacienda Posada de Vallina · Next to the Mezquita of Córdoba',see_rooms='See the rooms',hero_k='Córdoba · Jewish Quarter',hero_t='A historic inn next to the Mezquita',hero_s='In the heart of monumental Córdoba, a 1-minute walk from the Mosque-Cathedral.',
 intro_t='Tradition and comfort',intro_p1='An inn whose history goes back to the time of the Alarifes, in the Jewish Quarter, with a Cordoban patio.',
 intro_p2='24-hour reception, free wifi, bar, shared lounge with TV area, library and lift.',
 stats=['5 room types','Mezquita 1 min away','24 h reception','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Double, Twin, Economy double, Double with views and Double with extra bed, all with air conditioning and private bathroom.',
 svcs=['24-hour reception','Free wifi','Bar','Shared lounge and TV area','Library','Lift','Adapted for reduced mobility','24 h room service'],
 loc_p='Corregidor Luis de la Cerda, 83 · 14003 Córdoba. Mosque-Cathedral 1 minute, Roman Bridge 5 and Alcázar 7 minutes on foot.',
 chips=['What rooms does it have?','Where is it?','What services are there?','How do I book?']),
'fr':dict(title='Hotel Hacienda Posada de Vallina · À côté de la Mezquita de Cordoue',see_rooms='Voir les chambres',hero_k='Cordoue · Juderia',hero_t='Une auberge historique à côté de la Mezquita',hero_s='Au cœur de la Cordoue monumentale, à 1 minute à pied de la Mosquée-Cathédrale.',
 intro_t='Tradition et confort',intro_p1='Une auberge dont l\'histoire remonte à l\'époque des Alarifes, dans le quartier de la Juderia, avec un patio cordouan.',
 intro_p2='Réception 24h/24, wifi gratuit, bar, salon partagé avec coin TV, bibliothèque et ascenseur.',
 stats=['5 types de chambre','Mezquita à 1 min','Réception 24h/24','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Double, Twin, Double économique, Double avec vue et Double avec lit d\'appoint, toutes climatisées avec salle de bain privée.',
 svcs=['Réception 24h/24','Wifi gratuit','Bar','Salon partagé et coin TV','Bibliothèque','Ascenseur','Adapté aux personnes à mobilité réduite','Service en chambre 24h/24'],
 loc_p='Corregidor Luis de la Cerda, 83 · 14003 Cordoue. Mosquée-Cathédrale à 1 minute, Pont romain à 5 et Alcázar à 7 minutes à pied.',
 chips=['Quelles chambres a-t-il ?','Où est-il ?','Quels services propose-t-il ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://www.hhposadadevallina.es/bookingstep1/'; REN='https://www.hhposadadevallina.es/en/bookingstep1/'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':REN,'fr':REN})
D=dict(name='Hotel Hacienda Posada de Vallina',ac='#6b3a1f',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=[],foot=FOOT,
 address='Corregidor Luis de la Cerda, 83 · 14003 Córdoba',phones=['+34 957 49 87 50'],emails=['reservas@hhposadadevallina.es'],maps='Hotel Hacienda Posada de Vallina, Corregidor Luis de la Cerda 83, Córdoba',t=T)
META=dict(repo='demo-posada-del-vallina-cordoba',name='Hotel Hacienda Posada de Vallina',legal_name='Hotel Hacienda Posada de Vallina',registry_ids=['CIF B14787352'],
 url='https://www.hhposadadevallina.es/',domain='hhposadadevallina.es',municipality='Córdoba',province='Córdoba',sector='hotel en una posada histórica de la Judería de Córdoba, junto a la Mezquita',
 read_at='2026-10-29T15:20:00+01:00',created_at='2026-10-29T15:20:00+01:00',built_at='2026-10-29T15:30:00+01:00',audit_date='2026-10-29T14:55:00+01:00',
 rating=dict(value=4.1,coincide=['telefono','web'],date='2026-10-29T11:07:54+01:00',url='https://www.google.com/maps/place/Hotel+Hacienda+Posada+De+Vallina/@37.8782683,-4.7790682,17z/data=!4m9!3m8!1s0xd6d208330ddffdb:0x559b666e402d76a8!5m2!4m1!1i2!8m2!3d37.8782683!4d-4.7790682!16s%2Fg%2F1td2w7cd'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas del propio hotel (hhposadadevallina.es/bookingstep1, pagina del propio dominio que carga el componente de tarifas de Mirai del hotel, data-mirai-id 33778312; version /en/ para ingles y frances); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Hay habitación con vistas a la Mezquita?','K02'),('¿Tienen habitación para tres?','K03'),('¿Dónde está?','K04'),('¿A cuánto está la Mezquita?','K04'),('¿Qué servicios tiene?','K05'),('¿Está adaptado para silla de ruedas?','K06'),('¿Hay wifi?','K07'),('¿Tiene bar?','K08'),('¿Qué incluye la habitación?','K09'),('¿Cómo reservo?','K10'),('¿Quién es el titular?','K11'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Tienen piscina?',None),('¿Admiten mascotas?',None)],
'ca':[('Quines habitacions té?','K01'),('Hi ha habitació amb vistes a la Mesquita?','K02'),('Teniu habitació per a tres?','K03'),('On és?','K04'),('A quina distància és la Mesquita?','K04'),('Quins serveis té?','K05'),('Està adaptat per a cadira de rodes?','K06'),('Hi ha wifi?','K07'),('Té bar?','K08'),('Què inclou l\'habitació?','K09'),('Com reservo?','K10'),('Qui és el titular?','K11'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Teniu piscina?',None),('Admeteu mascotes?',None)],
'en':[('What rooms does it have?','K01'),('Is there a room with a view of the Mezquita?','K02'),('Do you have a room for three?','K03'),('Where is it?','K04'),('How far is the Mezquita?','K04'),('What services are there?','K05'),('Is it wheelchair accessible?','K06'),('Is there wifi?','K07'),('Is there a bar?','K08'),('What does the room include?','K09'),('How do I book?','K10'),('Who is the owner?','K11'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Is there a pool?',None),('Are pets allowed?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Y a-t-il une chambre avec vue sur la Mezquita ?','K02'),('Avez-vous une chambre pour trois ?','K03'),('Où est-il ?','K04'),('À quelle distance est la Mezquita ?','K04'),('Quels services propose-t-il ?','K05'),('Est-il accessible en fauteuil roulant ?','K06'),('Y a-t-il le wifi ?','K07'),('Y a-t-il un bar ?','K08'),('Que comprend la chambre ?','K09'),('Comment réserver ?','K10'),('Qui est le titulaire ?','K11'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Y a-t-il une piscine ?',None),('Les animaux sont-ils admis ?',None)]}
