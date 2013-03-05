
#ifndef RMSD_CUDA_SERIAL_H_
#define RMSD_CUDA_SERIAL_H_

#include <vector>
#include "../RMSDCalculator.h"

class QCPSerialCalculator: public RMSDCalculator{

	public:
		QCPSerialCalculator(int numberOfConformations, int atomsPerConformation, double* coords);
		virtual ~QCPSerialCalculator();
		
	protected:
		virtual void _one_vs_following_fit_equals_calc_coords(double* reference,
				int reference_conformation_number, double *rmsd);
		virtual void _one_vs_following_fit_differs_calc_coords(double* fitReference,
				double* calcReference, int reference_conformation_number, double *rmsd);
		virtual void _one_vs_following_fit_equals_calc_coords_changing_coordinates(double* reference,
				int reference_conformation_number, double *rmsd);
		virtual void _one_vs_following_fit_differs_calc_coords_changing_coordinates(double* fitReference,
				double* calcReference, int reference_conformation_number, double *rmsd);

		KernelFunctions* getKernelFunctions();

};

#endif