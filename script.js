var sourceImg = document.getElementById("src-img");
var imgUplaod = document.getElementById("fileUpload")


// get input color 
function getInputColor() {
    var colors = document.getElementsByName("color")
    
    // color selector var 
    var colorHolder = ""

    for(let i=0; i<colors.length; i++) {
        if (colors[i].checked) {
            colorHolder = colors[i].value
        }
    }
    return colorHolder
}

// onload handler for removing the welcome text after openCV is loading 
window.onOpenCvReady = function () {
    document.getElementById("welcomeMsg").remove()
}

imgUplaod.onchange = function () {
    sourceImg.src = URL.createObjectURL(event.target.files[0])
}
//display the other modified img
sourceImg.onload = function () {
    //getting user choice of color
    var colorChoice = getInputColor()

    //loading the image

    if (colorChoice === "defaultColor"){
        //display the color with no effects 
        let sourceMat = cv.imread(sourceImg)
        cv.imshow("edited-img", sourceMat)
        sourceMat.delete()

    }else{

        let sourceMat = cv.imread(sourceImg)
        let destMat = sourceMat.clone()
        
        cv.cvtColor(sourceMat, destMat, cv.COLOR_RGBA2GRAY)
        cv.imshow("edited-img", destMat)
        
        // deleting 
        destMat.delete()
        sourceMat.delete()

    }

}

