module FFT where

import Data.Complex

phaseRot :: RealFloat a => Int -> Complex a -> Int -> Complex a
phaseRot nSmpls x m = x * cis(-2 * pi * fromIntegral(m) / fromIntegral(nSmpls))

splitByParity :: [a] -> ([a], [a])
splitByParity [] = ([], [])
splitByParity [x] = ([x], [])
splitByParity (x:y:zs) = (x:xt, y:yt) where (xt, yt) = splitByParity zs  

fft :: RealFloat a => [Complex a] -> [Complex a]
fft [] = []
fft [x] = [x]
fft [x, y] = [x + y, x - y]
fft zs = (zipWith (+) es rotOs) ++ (zipWith (-) es rotOs)
    where es = fft evens
          rotOs = zipWith (phaseRot (length zs)) os [0..]
          os = fft odds
          (evens, odds) = splitByParity zs
