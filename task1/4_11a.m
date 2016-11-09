function ret = f(x,t)
    x_1(1) = 1.5 - t * (0.01*x(1)^3*x(2)^2-0.001*cos(x(1)^2*x(2)))/2;
    x_1(2) = -0.5 - t * (0.01*x(1)^3*x(2)^2+0.001*cos(x(1)^2*x(2)))/2;
    ret = x_1;
end

n = 0;
for t = 0.0:0.01:1
    n = n + 1;
    x = [0.1; 0.1];
    for i = 0:1000
        x = f(x, t);
    end
    t, x
    u1(n) = x(1);
    v1(n) = x(2);
end

plot(u1, v1, "ob");
