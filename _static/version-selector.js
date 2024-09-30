document.addEventListener("DOMContentLoaded", function() {
    var versionSelector = document.querySelector('#version-selector select');

    fetch('/_static/versions.json') // Adjust the path to where you host versions.json
        .then(function(response) {
            return response.json();
        })
        .then(function(versions) {
            versions.forEach(function(v) {
                var option = new Option(v.version, v.url);
                // Set the current version as selected
                if (window.location.pathname.includes(v.url)) {
                    option.selected = true;
                }
                versionSelector.add(option);
            });
        });

    versionSelector.onchange = function() {
        window.location.href = this.value;
    };
});

