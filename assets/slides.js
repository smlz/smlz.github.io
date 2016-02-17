(function($) {
    var options = {
      highlightStyle: "default",
      navigation: {
        scroll: false,
        touch: false,
        click: true
      },
      ratio: "4:3",
      slideNumberFormat: '%current%',
      countIncrementalSlides: false
    };
    if (typeof $.urlParam !== 'undefined' && $.urlParam("source")) {
        options.sourceUrl = $.urlParam("source");
    }
    remark.create(options);
})((typeof jQuery !== 'undefined' ? jQuery : (window.jQuery = {})));
