var sourceImg = document.getElementById("src-img");
var imgUplaod = document.getElementById("fileUpload")

// onload handler for removing the welcome text after openCV is loading 
window.onOpenCvReady = function () {
    document.getElementById("welcomeMsg").remove()
}

imgUplaod.onchange = function () {
    sourceImg.src = URL.createObjectURL(event.target.files[0])
}
//display the other modified img
sourceImg.onload = function () {
    //loading the image
    let sourceMat = cv.imread(sourceImg)
    let destMat = sourceMat.clone()

    cv.cvtColor(sourceMat, destMat, cv.COLOR_RGBA2GRAY)
    cv.imshow("edited-img", destMat)

    destMat.delete()
    sourceMat.delete()
}

