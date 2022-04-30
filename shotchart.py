import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def draw_plotly_court(fig, fig_width=600, margins=10):
        
    # From: https://community.plot.ly/t/arc-shape-with-path/7205/5
    def ellipse_arc(x_center=0.0, y_center=0.0, a=10.5, b=10.5, start_angle=0.0, end_angle=2 * np.pi, N=200, closed=False):
        t = np.linspace(start_angle, end_angle, N)
        x = x_center + a * np.cos(t)
        y = y_center + b * np.sin(t)
        path = f'M {x[0]}, {y[0]}'
        for k in range(1, len(t)):
            path += f'L{x[k]}, {y[k]}'
        if closed:
            path += ' Z'
        return path

    fig_height = fig_width * (470 + 2 * margins) / (500 + 2 * margins)
    fig.update_layout(width=fig_width, height=fig_height)

    # Set axes ranges
    fig.update_xaxes(range=[-250 - margins, 250 + margins])
    fig.update_yaxes(range=[-52.5 - margins, 417.5 + margins])

    threept_break_y = 89.47765084
    three_line_col = "#777777"
    main_line_col = "#777777"

    fig.update_layout(
        # Line Horizontal
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white",
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False,
            fixedrange=True,
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False,
            fixedrange=True,
        ),
        shapes=[
            dict(
                type="rect", x0=-250, y0=-52.5, x1=250, y1=417.5,
                line=dict(color=main_line_col, width=1),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="rect", x0=-80, y0=-52.5, x1=80, y1=137.5,
                line=dict(color=main_line_col, width=1),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="rect", x0=-60, y0=-52.5, x1=60, y1=137.5,
                line=dict(color=main_line_col, width=1),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="circle", x0=-60, y0=77.5, x1=60, y1=197.5, xref="x", yref="y",
                line=dict(color=main_line_col, width=1),
                # fillcolor='#dddddd',
                layer='below'
            ),
            dict(
                type="line", x0=-60, y0=137.5, x1=60, y1=137.5,
                line=dict(color=main_line_col, width=1),
                layer='below'
            ),

            dict(
                type="rect", x0=-2, y0=-7.25, x1=2, y1=-12.5,
                line=dict(color="#ec7607", width=1),
                fillcolor='#ec7607',
            ),
            dict(
                type="circle", x0=-7.5, y0=-7.5, x1=7.5, y1=7.5, xref="x", yref="y",
                line=dict(color="#ec7607", width=1),
            ),
            dict(
                type="line", x0=-30, y0=-12.5, x1=30, y1=-12.5,
                line=dict(color="#ec7607", width=1),
            ),

            dict(type="path",
                 path=ellipse_arc(a=40, b=40, start_angle=0, end_angle=np.pi),
                 line=dict(color=main_line_col, width=1), layer='below'),
            dict(type="path",
                 path=ellipse_arc(a=237.5, b=237.5, start_angle=0.386283101, end_angle=np.pi - 0.386283101),
                 line=dict(color=main_line_col, width=1), layer='below'),
            dict(
                type="line", x0=-220, y0=-52.5, x1=-220, y1=threept_break_y,
                line=dict(color=three_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-220, y0=-52.5, x1=-220, y1=threept_break_y,
                line=dict(color=three_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=220, y0=-52.5, x1=220, y1=threept_break_y,
                line=dict(color=three_line_col, width=1), layer='below'
            ),

            dict(
                type="line", x0=-250, y0=227.5, x1=-220, y1=227.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=250, y0=227.5, x1=220, y1=227.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=17.5, x1=-80, y1=17.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=27.5, x1=-80, y1=27.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=57.5, x1=-80, y1=57.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=87.5, x1=-80, y1=87.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=90, y0=17.5, x1=80, y1=17.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=90, y0=27.5, x1=80, y1=27.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=90, y0=57.5, x1=80, y1=57.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=90, y0=87.5, x1=80, y1=87.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),

            dict(type="path",
                 path=ellipse_arc(y_center=417.5, a=60, b=60, start_angle=-0, end_angle=-np.pi),
                 line=dict(color=main_line_col, width=1), layer='below'),

        ]
    )
    return True



from copy import deepcopy
teamname = 'OKC'
league_hexbin_stats = pd.read_pickle('/Users/amos/Downloads/basketballplots/league_hexbin_stats.pickle')
team_hexbin_stats = pd.read_pickle('/Users/amos/Downloads/basketballplots/' + teamname.lower() + '_hexbin_stats.pickle')

def filt_hexbins(hexbin_stats, min_threshold=0.0):

    from copy import deepcopy

    filt_hexbin_stats = deepcopy(hexbin_stats)
    temp_len = len(filt_hexbin_stats['freq_by_hex'])
    filt_array = [i > min_threshold for i in filt_hexbin_stats['freq_by_hex']]
    for k, v in filt_hexbin_stats.items():
        if type(v) != int:
            if len(v) == temp_len:
                filt_hexbin_stats[k] = [v[i] for i in range(temp_len) if filt_array[i]]

    return filt_hexbin_stats

rel_hexbin_stats = deepcopy(team_hexbin_stats)
base_hexbin_stats = deepcopy(league_hexbin_stats)
rel_hexbin_stats['accs_by_hex'] = rel_hexbin_stats['accs_by_hex'] - base_hexbin_stats['accs_by_hex']
rel_hexbin_stats = filt_hexbins(rel_hexbin_stats, min_threshold=0.0)
max_freq = 0.002
xlocs = rel_hexbin_stats['xlocs']
ylocs = rel_hexbin_stats['ylocs']
accs_by_hex = rel_hexbin_stats['accs_by_hex']
freq_by_hex = np.array([min(max_freq, i) for i in rel_hexbin_stats['freq_by_hex']])

colorscale = 'RdYlBu_r'
marker_cmin = -0.05
marker_cmax = 0.05
title_txt = teamname + ":<BR>Shot chart, '18-'19<BR>(vs NBA average)"

hexbin_text = [
        '<i>Accuracy: </i>' + str(round(accs_by_hex[i]*100, 1)) + '% (vs league avg)<BR>'
        '<i>Frequency: </i>' + str(round(freq_by_hex[i]*100, 2)) + '%'
        for i in range(len(freq_by_hex))
]
ticktexts = ["Worse", "Average", "Better"]
logo_url = "https://d2p3bygnnzw9w3.cloudfront.net/req/202001161/tlogo/bbr/" + teamname + ".png"

fig = go.Figure()
draw_plotly_court(fig, fig_width=600)
fig.add_trace(go.Scatter(
    x=xlocs, y=ylocs, mode='markers', name='markers',
    text=hexbin_text,
    marker=dict(
        size=freq_by_hex, sizemode='area', sizeref=2. * max(freq_by_hex) / (11. ** 2), sizemin=2.5,
        color=accs_by_hex, colorscale=colorscale,
        colorbar=dict(
            thickness=15,
            x=0.84,
            y=0.87,
            yanchor='middle',
            len=0.2,
            title=dict(
                text="<B>Accuracy</B>",
                font=dict(
                    size=11,
                    color='#4d4d4d'
                ),
            ),
            tickvals=[marker_cmin, (marker_cmin + marker_cmax) / 2, marker_cmax],
            ticktext=ticktexts,
            tickfont=dict(
                size=11,
                color='#4d4d4d'
            )
        ),
        cmin=marker_cmin, cmax=marker_cmax,
        line=dict(width=1, color='#333333'), symbol='hexagon',
    ),
    hoverinfo='text'
))

fig.update_layout(
    title=dict(
        text=title_txt,
        y=0.9,
        x=0.19,
        xanchor='left',
        yanchor='middle'),
    font=dict(
        family="Arial, Tahoma, Helvetica",
        size=10,
        color="#7f7f7f"
    ),
    annotations=[
        go.layout.Annotation(
            x=0.5,
            y=0.05,
            showarrow=False
        ),
    ],
)

fig.add_layout_image(
    go.layout.Image(
        source=logo_url,
        xref="x", yref="y", x=-230, y=405, sizex=50, sizey=50,
        xanchor="left", yanchor="top",
        sizing="stretch", opacity=1, layer="above"))


st.plotly_chart(fig, use_container_width=True)