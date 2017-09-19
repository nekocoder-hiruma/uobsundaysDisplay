
(function(){
    var tabLength = $('.gallery-tab-content > div.content').length + 1;
    for(tabloop = 1; tabloop < tabLength; tabloop++){
        $('<li class="tab-title"><a href="#page' + tabloop + '">' + tabloop + '</a></li>').appendTo('.gallery-tabs');
    }
    var galleryTabs = $('ul.gallery-tabs li:nth-child(1)');
    galleryTabs.addClass('active');
}());
