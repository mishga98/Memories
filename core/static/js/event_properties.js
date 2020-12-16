ymaps.ready(init);
var myMap;
var myGeoObject = null;
function init () {
    myMap = new ymaps.Map("map", {
        center: [56.0071, 92.8601], // Красноярск
        zoom: 11
    }, {
        balloonMaxWidth: 200,
        searchControlProvider: 'yandex#search'
    });



    // Обработка события, возникающего при щелчке
    // левой кнопкой мыши в любой точке карты.
    // При возникновении такого события откроем балун.
    myMap.events.add('click', function (e) {
        if (!myMap.balloon.isOpen()) {
            var coords = e.get('coords');
            myMap.balloon.open(coords, {
                contentHeader:'Отлично!',
                contentBody:'<p>Теперь сохраните заметку</p>' +
                    '<p>Координаты: ' + [
                    coords[0].toPrecision(6),
                    coords[1].toPrecision(6)
                    ].join(', ') + '</p>',
                contentFooter:'<sup>Или вы можете выбрать другое место</sup>'
            });
        }
        else {
            myMap.balloon.close();
        }
        var coords = e.get('coords');
        document.getElementById('coord_id').value=[
                    coords[0].toPrecision(6),
                    coords[1].toPrecision(6)
                    ].join(', ');

        if (myGeoObject!=null)  {
            myGeoObject.geometry.setCoordinates([coords[0], coords[1]])
            }
        else {
            myGeoObject = new ymaps.Placemark([coords[0], coords[1]], {
                    balloonContent: ''
                }, {
                    preset: 'islands#darkGreenDotIcon',
                    iconCaptionMaxWidth: '50'
                })
            myMap.geoObjects.add(myGeoObject);
        }
    });



    // Обработка события, возникающего при щелчке
    // правой кнопки мыши в любой точке карты.
    // При возникновении такого события покажем всплывающую подсказку
    // в точке щелчка.
    myMap.events.add('contextmenu', function (e) {
        myMap.hint.open(e.get('coords'), 'Кто-то щелкнул правой кнопкой');
    });
    
    // Скрываем хинт при открытии балуна.
    myMap.events.add('balloonopen', function (e) {
        myMap.hint.close();
    });
}