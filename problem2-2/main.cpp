#include <iostream>
#include <functional>
#include <vector>
#include <cmath>
#include <fstream>
#include <cstdlib>

//u_t +  a(x, t) * u_x = f(x, t)

inline double a(double x, double t)
{
    return exp(t);
}

inline double phi(double x)
{
    return (x - 1)*(x - 1);
}

inline double psi(double t)
{
    return exp(2*t) + 0.5*t*t;
}

inline double f(double x, double t)
{
    return t;
}

void generateData(std::vector<double> u, std::ofstream& data_file, double t, double h)
{
    for (size_t x_index = 0; x_index < u.size(); ++x_index)
        data_file << x_index*h << " " << t << " " << u[x_index] << std::endl; 
}

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        std::cerr << "usage: " << argv[0] <<  " [data_file] [tau] [h]\n";
        return -1;
    }

    double tau = atof(argv[2]);
    double h = atof(argv[3]);

    if ((tau <= 0) || (h <= 0))
    {
        std::cerr << "Invalid aruments.\n";
        return -1;        
    }

    size_t t_num = static_cast<size_t>(1 / tau) + 1;
    size_t x_num = static_cast<size_t>(1 / h) + 1;

    std::vector<double> u(x_num);

    std::ofstream data_file(argv[1], std::ios::out | std::ios::trunc);
    if (!data_file.is_open())
    {
        std::cout << "Unable to open file.\n";
        return -1;
    }
    data_file << std::fixed;

    for (size_t x_index = 0; x_index < x_num; ++x_index)
        u[x_index] = phi(x_index * h);
    generateData(u, data_file, 0, h);

    for (size_t t_index = 1; t_index < t_num; ++t_index)
    {
        for (size_t x_index = x_num - 1; x_index > 0; --x_index)
            u[x_index] = u[x_index] - tau/h*a(x_index*h, t_index*tau)*(u[x_index] - u[x_index - 1]) + tau*f(0, tau*t_index);
        u[0] = psi(t_index*tau);
        generateData(u, data_file, t_index*tau, h);
    }

    data_file.close();
}
