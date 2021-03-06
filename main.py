
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 1) выбор типа характеристики: "turbine" или "compressor"
    type_of_map="compressor" #!!!
    # 2) указать адрес к файлу с исходниками характеристики
    # обычно это текстовый файл (например csv) с колонками формата: "n;G;PR;Eff" , также для турбины могут дополнительно быть два столбика "A;L"
    # где n  - приведенные обороты
    # G -  приведенный расход для компрессора или пропускная способность для турбины
    # PR - степень повышения давления в компрессоре или степень понижения давления для турбины
    # Eff - изоэнтропический (адиабатный) кпд
    # A - осредненный угол выхода потока из турбины (иногда используется для расчета характеристик потерь на выходе из турбины)
    # L - осредненная скорость потока на выходе из турбины (иногда используется для расчета характеристик потерь на выходе из турбины)
    name_of_file = "\\2020 11 аэродинамические характеристики компрессора ГТЭ-170 по результатам CFD\\AC CFD 2020 11 A+3.csv"
    from kernel import *

    test=approximator(type=type_of_map, name_of_file=name_of_file, print_plot=False)
    test.stage1_extrapolation(print_plot=False)
    test.stage2_check_interpolation_along_n_curve_const(print_plot=False)
    test.stage3(print_plot=False)
    test.stage4(print_plot=True)
    plt.show()
