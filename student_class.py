class students:

    def calculate(self):
        selfa = int(input('Enter the marks of suba: '))
        selfb = int(input('Enter the marks of subb: '))
        selfc = int(input('Enter the marks of subc: '))
        selfd = int(input('Enter the marks of subd: '))
        selfe = int(input('Enter the marks of sube: '))
        add = selfa + selfb + selfc + selfd + selfe
        avg = (selfa + selfb + selfc + selfd + selfe) / 5
        percentage = (selfa + selfb + selfc + selfd + selfe) * 100 / 500
        print 'addition is %f' % add
        print 'average is %f' % avg
        print 'percentage is %f' % avg


c = students()
c.calculate()
