##################################
##  Author: Tianyang Zhang
##  Contact: keavilzhangzty@gmail.com

from visdom import Visdom


class VisdomVisualizer(object):
    def __init__(self, envid, run_name, xaxis_name='Timestep', yaxis_name='Return', server='http://168.62.48.224', port=5000):
        self.viz = Visdom(server=server, port=port)
        assert self.viz.check_connection()  
        self.run_name = run_name
        self.traces = {}
        self.win = None
        self.envid = envid
        self.layout = dict(
            title=run_name, 
            xaxis={'title': xaxis_name}, 
            yaxis={'title': yaxis_name}
            )
        self.data = {}

    def initialize(self, name, color):
        self.data[name] = dict(x=[], y=[], y_upper=[], y_lower=[])
        self.traces[name] = dict(
            x=[], y=[], name=name,
            line=dict(color=color, width=3),
            mode="lines", type='custom'
            )

    def send(self):
        try:
            self.win=self.viz._send({
                'data':list(self.traces.values()), 
                'layout':self.layout, 
                'win':self.win,
                'eid':self.envid,
                })
        except:
            print('Error: Send graph error! This error will be ignored.')
            self.win = None

    def paint(self, name, data: dict):
        for key, val in data.items():
            self.data[name][key].append(float(val))

    def draw_line(self, name, color):
        x, y = self.data[name]['x'], self.data[name]['y']
        self.traces[name] = dict(
            x=x, y=y, name=name, 
            line=dict(color=color, width=3),
            mode="lines", type='custom'
            )
        self.send()

    def fill_line(self, name, color):
        x, y_upper, y_lower = self.data[name]['x'], self.data[name]['y_upper'], self.data[name]['y_lower']
        name = name + '_fill'
        self.traces[name] = dict(
            x=x+x[::-1], 
            y=y_upper+y_lower[::-1],
            name=name,
            line=dict(color='rgba(255,255,255,0)'),
            fill='tozerox',
            fillcolor=color,
            showlegend=True,
            type='custom'
            )
        self.send()

#
if __name__ == '__main__':
    v = VisdomVisualizer('pushi-atari' ,'Venture-divergence')
    v.initialize('train-reward', 'red')
    v.paint('train-reward', {'x':1, 'y':2})
    v.initialize('test-reward', 'cyan')
    v.paint('test-reward', {'x':1, 'y':3})
    v.paint('test-reward',{'x':2, 'y':2})
    v.paint('train-reward', {'x':2, 'y':3})
    v.paint('test-reward', {'x':3, 'y':1})
    v.paint('train-reward', {'x':3, 'y':4})

    v.draw_line('test-reward', 'rgb(255, 0, 0)')
    v.draw_line('train-reward', 'rgb(0, 0, 255)')
    #v.fill_line('sth_fill', 'rgba(0, 100, 80, 0.2)', [0, 1, 2, 3, 4], [0, 6, 8, 2, 4], [0, 4, 6, 0, 2])
    #v.fill_line('sth_fill', 'rgba(0, 100, 80, 0.2)', [5, 6, 7, 8, 9], [4, 6, 8, 2, 4], [2, 4, 6, 0, 2])
