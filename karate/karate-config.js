function fn() {
    var apiKey = java.lang.System.getenv("HOME");
    karate.log(apiKey);
    return {
        ALMA_APIKEY: apiKey,
    };
}