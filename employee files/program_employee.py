from worker import Worker
from manager import Manager
from contractor import Contractor

def main():
    jeffbazos = Worker(32,'Jeff Bazos', 'Amazon Av.', 45, 1976, 9, 31 )
    elonmusk = Worker(55,'Elom Musk', 'Tesla Dr.', 39, 1982, 7, 48)
    boris = Manager(1, 'Boris Musnikov', 'Rashi31', 29, 1992, 2, 424242424242)
    bibi = Contractor (2000, 'Bibi Matanyahu', 'Knesset St.', 210, 1811, 1000, 80000)

    print(jeffbazos)
    print(jeffbazos.get_age())
    print(jeffbazos.calc_sal_worker())
    print(elonmusk)
    print(elonmusk.get_age())
    print(elonmusk.calc_sal_worker())
    print(boris)
    print(boris.calc_sal_manager())
    print(bibi)
    print(bibi.calc_sal_contractor())

main()