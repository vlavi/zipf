
import argparse
import pandas as pd


def main(args):
    input_csv = args.infile
    output_png = args.outfile
    df = pd.read_csv(input_csv, header=None, names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False, 
method='max')
    df['inverse_rank'] = 1 / df['rank']
    scatplot = df.plot.scatter(x='word_frequency',
                               y='rank', loglog = True,
                               figsize=[12, 6],
                               grid=True)
    ax = df.plot.scatter(x='word_frequency',
                         y='inverse_rank',
                         figsize=[12, 6],
                         grid=True,
                         xlim=args.xlim)
    ax.figure.savefig(args.outfile)


if __name__ == '__main__':
    USAGE = 'Brief description of what the script does.'
    parser = argparse.ArgumentParser(description=USAGE)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Word count csv file name')
    parser.add_argument('--outfile', type=str, 
                        default='plotcounts.png',
                        help='Output image file name')
    parser.add_argument('--xlim', type=float, default=None,
                        nargs=2,
                        metavar=('XMIN', 'XMAX'),
                        help='X-axis bounds')
    args = parser.parse_args()
    main(args)
