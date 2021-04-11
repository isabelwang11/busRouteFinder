let box

let app = new Phaser.Game({
  type: Phaser.CANVAS,
  width: window.innerWidth,
  height: window.innerHeight,
  backgroundColor: '#efefef',
  scene: {
    preload() {
      this.load.svg('map', 'METRO_System_Map.svg')
    },
    create() {
      this.add.image(400, 300, 'map')
      box = new Phaser.Rectangle(0, 550, 800, 50)
    }
  }
})

L.mapquest.key = 'OHJGwJkOJt3B0j2xd3OEwK02tJWi8z9Y';

// 'map' refers to a <div> element with the ID map
L.mapquest.map('map', {
  center: [37.7749, -122.4194],
  layers: L.mapquest.tileLayer('map'),
  zoom: 12
});

var map = new mqgl.Map('map', 'OHJGwJkOJt3B0j2xd3OEwK02tJWi8z9Y', {
    center: [-122.2082454,37.4780123],
    zoom: 13,
    pitch: 60,
    bearing: 0
  });
  
  map.load(function() {
    setTimeout(function() {
      map.map.flyTo({speed: 0.5, zoom: 15, pitch: 60, bearing: 180, center: [-122.3989808,37.7517676]})
    }, 2000);
  });