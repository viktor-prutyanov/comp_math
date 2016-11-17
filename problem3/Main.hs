module Main where

import System.Environment
import Data.Complex
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
    [inFile] <- getArgs
    s <- readFile inFile
    print (map (\z -> roundComplex z 10) (fft (toComplexDoubleList s)))
