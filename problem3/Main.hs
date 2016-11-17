module Main where

import System.Environment
import Data.Complex
import Data.List
import FFT (fft)

roundNSigns :: RealFloat x => x -> Int -> x  
roundNSigns x nSigns = fromIntegral(round(realToFrac(x) * eps)) / eps
    where eps = 10 ^ nSigns

roundComplex :: RealFloat z => Complex z -> Int -> Complex z
roundComplex z nSigns = (roundNSigns (realPart z) nSigns) :+ (roundNSigns (imagPart z) nSigns)

toComplexDoubleList s = map strToInt (lines s)
    where strToInt = read :: String -> Complex Double

main :: IO ()
main = do
    [inFile, outFile] <- getArgs
    s <- readFile inFile
    writeFile outFile $ intercalate "\n" $ map show $ map (\z -> roundComplex z 10) $ fft $ toComplexDoubleList s
