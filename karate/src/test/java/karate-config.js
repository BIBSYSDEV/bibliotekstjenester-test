function setup() {
    const primoApiKey = java.lang.System.getenv("primoApiKey");
    const almaApiKey = java.lang.System.getenv("almaApiKey");
    return {
        PRIMO_APIKEY: primoApiKey,
        ALMA_APIKEY: almaApiKey,
    };
}