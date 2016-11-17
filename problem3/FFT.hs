module FFT where

import Data.Complex
import Data.List (partition)
import Control.Arrow

phaseRot :: RealFloat a => Int -> Complex a -> Int -> Complex a
phaseRot nSmpls x m = x * cis(-2 * pi * fromIntegral(m) / fromIntegral(nSmpls))

fft :: RealFloat a => [Complex a] -> [Complex a]
fft [] = []
fft [x] = [x]
fft [x, y] = [x + y, x - y]
fft zs = (zipWith (+) es rotOs) ++ (zipWith (-) es rotOs)
    where es = fft evens
          rotOs = zipWith (phaseRot (length zs)) os [0..]
          os = fft odds
          (evens, odds) = ((map fst) *** (map fst)) (partition (\(x,y) -> even y) (zip zs [0..])) 
