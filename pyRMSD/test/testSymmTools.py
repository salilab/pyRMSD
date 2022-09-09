"""
Created on 29/07/2013

@author: victor
"""
import unittest
from pyRMSD.symmTools import  symm_permutations, swap_atoms, min_rmsd_of_rmsds_list, symm_groups_validation
from pyRMSD.symmTools import symm_groups_validation_new, symm_permutations_new
import numpy


class Test(unittest.TestCase):

    def test_validation(self):
        symm_group_1 = [ [1,2] ] # This is a single symm group. It means that atom 1 and 2 are equivalent. We will try 
                                # to swap 1 and 2.
                                 
        symm_group_2 = [ [3,4],[5,6] ]  # This is a single symm group. It means that atom 3 and 4, as well as 
                                        # atoms 5,6 are equivalent, and they have to be swapped at the same time. 
                                        # We will try with the following combinations:
                                        # (3,4)  (5,6)
                                        # (4,3)  (6,5)
        
        symm_group_3 = [ [1,2,3],[4,5,6] ]  # multi-unit symm group, Atoms 1, 2, 3 are equivalent and so are 4, 5, 6
        # The validation function validates a list of this symmetry groups. When we use this list, all permutations are
        # used (i.e. sym_perm(symm_group_1) x sym_perm(symm_group_2)). That is:
        # (1,2) (3,4)  (5,6)
        # (1,2) (4,3)  (6,5)
        # (2,1) (3,4)  (5,6)
        # (2,1) (4,3)  (6,5)

        # A symm group is not a valid description
        self.assertRaises(ValueError, symm_groups_validation, symm_group_1)
        
        # A list of symm groups is a valid symmetry descriptor
        try:
            symm_groups_validation([symm_group_1])
            symm_groups_validation([symm_group_1, symm_group_2])
        except ValueError:
            self.fail("Value exception has been raised.")
    
        # Old validation check fails
        self.assertRaises(ValueError, symm_groups_validation, [symm_group_3])
        # New validation check passes
        symm_groups_validation_new([symm_group_3])

    def test_symm_group_permutations(self):
        groups = [
                  [ [1,2] ],
                  [ [3,4],[5,6] ]
                  ]
        
        expected_permutations = [
                                    [ [[1,2]], [[3,4], [5,6]]],
                                    [ [[1,2]], [[4,3], [6,5]]],
                                    [ [[2,1]], [[3,4], [5,6]]],
                                    [ [[2,1]], [[4,3], [6,5]]]
                                ]
        
        
        for i, perm in enumerate(symm_permutations(groups)):
            self.assertSequenceEqual(expected_permutations[i], perm)
            
    def test_symm_group_permutations_new(self):
        """
        Tests the generation of permutations for symm-groups containing more than 2 elements per group
        """
        groups = [
                  [ [1,2] ],
                  [ [3,4,5],[6,7,8] ]
                  ]
        
        expected_permutations = [
                                    [ [[1,2]], [[3,4,5], [6,7,8]]],
                                    [ [[1,2]], [[3,5,4], [6,8,7]]],
                                    [ [[1,2]], [[4,3,5], [7,6,8]]],
                                    [ [[1,2]], [[4,5,3], [7,8,6]]],
                                    [ [[1,2]], [[5,3,4], [8,6,7]]],
                                    [ [[1,2]], [[5,4,3], [8,7,6]]],
                                    [ [[2,1]], [[3,4,5], [6,7,8]]],
                                    [ [[2,1]], [[3,5,4], [6,8,7]]],
                                    [ [[2,1]], [[4,3,5], [7,6,8]]],
                                    [ [[2,1]], [[4,5,3], [7,8,6]]],
                                    [ [[2,1]], [[5,3,4], [8,6,7]]],
                                    [ [[2,1]], [[5,4,3], [8,7,6]]],
                                ]
        
        all_perms = []
        for i, perm in enumerate(symm_permutations_new(groups)):
            all_perms.append(perm)
            
        all_perms = sorted(all_perms)
        expected_permutations = sorted(expected_permutations)
        self.assertListEqual(all_perms, expected_permutations)
        
        # test for empty permutation set
        groups = []
        all_perms = [i for i in symm_permutations_new(groups)]
        self.assertEqual(len(all_perms), 1)
        self.assertEqual(len(all_perms[0]), 0)
            
    def test_swap_atoms(self):
        coordsets = numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
        swap_atoms(coordsets, 0, 2)
        numpy.testing.assert_array_equal([[7, 8, 9],[4, 5, 6],[1, 2, 3],[10, 11, 12]], coordsets)
        
    def test_min_rmsd_of_rmsds_list(self):
        rmsds_list = numpy.array([[1,2,3,4],[4,3,2,1],[3,4,1,2]])
        calc_rmsds = min_rmsd_of_rmsds_list(rmsds_list)
        numpy.testing.assert_array_equal([1,2,1,1], calc_rmsds)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_symm_group_permutations']
    unittest.main()