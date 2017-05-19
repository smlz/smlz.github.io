var app = new Vue({
  el: "#app",
  data: {
    mitteilung: "Guten Tag!",
    vorname: "Marco",
    nachname: "Schmalz",
    name: "",
    nameGesetzt: false,
    icons: [
      {
        title: 'alt',
        url: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Grace_Hopper.jpg/220px-Grace_Hopper.jpg"
      },
      {
        title: 'jung',
        url: "https://qph.ec.quoracdn.net/main-qimg-99057870ca7da859d37f188c6a4aa1d4-c"
      }
    ]
  },
  methods: {
    namenAktualisieren: function() {
      this.name = this.vorname + " " + this.nachname;
      this.nameGesetzt = true;
    }
  }
});

setTimeout(function() {
  app.mitteilung = 'Guten Abend!';
}, 2000);
