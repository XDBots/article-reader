isValidURL = function(url){
    
    const regex = new RegExp('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+');
    return regex.test(url) // returns boolean 

}

module.exports= isValidURL;