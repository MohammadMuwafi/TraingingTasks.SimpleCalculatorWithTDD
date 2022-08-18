import pytest
import simple_calculator as sc

def test_simple_calculator():
    assert sc.add("") == 0
    assert sc.add("5,3,2") == 10
    assert sc.add("1,,2") == -1
    assert sc.add("1,2") == 3
    assert sc.add("1,2,1,2,") == -1
    assert sc.add("1,2,1,2,1") == 7

    assert sc.add("1,2,1,2\n,1") == -1
    assert sc.add("1\n2,1,2\n1") == 7

    assert sc.add("/1\n2,1,2\n1") == -1
    assert sc.add("//") == -1
    assert sc.add("//,.\n") == 0
    assert sc.add("//[,]\n2,1") == 3
    assert sc.add("//,\n2,1") == 3
    assert sc.add("//[.][,]\n2,1,2.1") == 6
    assert sc.add("//[.][,]\n2,1,2!1") == -1
    
    with pytest.raises(Exception) as exec_info:
        sc.add("-134,1,-2,-3,-4")
    
    try:
        sc.add("-134,-1")
    except Exception as e: 
        assert "negatives not allowed -134 -1" == str(e)

    assert sc.add("1,24,1001") == 25

    assert sc.add("//[***][!!!][#][!!]\n1***2***3!!!444#234!!23") == 684 + 23
