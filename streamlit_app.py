import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import datetime as datetime

from zones import hrRunZones, runPaceZones, hrBikeZones, powerBikeZones, swimPaceZones

# some text to explain the purpose of the app
st.title('Calculate your training zones')
st.text('This app calculates your training zones for triathlon based on test results.\nThe tests include the following:')

col1_1, col1_2, col1_3 = st.columns([0.6,1.6,3])

col1_1.write('Discipline')
col1_1.text('Run')
col1_1.text('Bike')
col1_1.text('Swim')

col1_2.write('Test Description')
col1_2.text('20 min all-out effort')
col1_2.text('20 min FTP test')
col1_2.text('1000 m all-out swim')

col1_3.write('Test Result')
col1_3.text('Average HR [BPM] + Average Pace [mm:ss/1000 m]')
col1_3.text('Average HR [BPM] + Average Power [W]')
col1_3.text('Average Pace [mm:ss/100 m]')

# define test conditions and discipline

st.sidebar.header('Input your data')
st.sidebar.write('Select the input accordingly')

date = st.sidebar.date_input('Select the date of the test')

discipline = st.sidebar.radio('Select your discipline:', ['none', 'Run', 'Bike', 'Swim'])
if discipline == 'Run':
    testResults = st.sidebar.multiselect('Test Results', ['Heart Rate', 'Pace'])
if discipline == 'Bike':
    testResults = st.sidebar.multiselect('Test Results', ['Heart Rate', 'Power'])

if discipline == 'Run':
    if 'Heart Rate' in testResults:
        hrBounds = st.sidebar.slider(
            'Select minimum and maximum heart rate [BPM]',
            0, 220, (50, 190))
        runTestAvgHR = st.sidebar.number_input('Input test average heart rate [BPM]', min_value=100, max_value=220,
                                               value=175, step=1)
        st.write(hrRunZones(runTestAvgHR, hrBounds).df.style.format("{:.0f}"))
    if 'Pace' in testResults:
        runTestAvgPace = st.sidebar.text_input('Input test average pace [mm:ss]', value='5:00')
        results_in_seconds = runPaceZones(runTestAvgPace).list

        results_in_minutes_list = [[str(datetime.timedelta(seconds=results_in_seconds[0][0])),
                                    str(datetime.timedelta(seconds=results_in_seconds[0][1]))],
                                   [str(datetime.timedelta(seconds=results_in_seconds[1][0])),
                                    str(datetime.timedelta(seconds=results_in_seconds[1][1]))],
                                   [str(datetime.timedelta(seconds=results_in_seconds[2][0])),
                                    str(datetime.timedelta(seconds=results_in_seconds[2][1]))],
                                   [str(datetime.timedelta(seconds=results_in_seconds[3][0])),
                                    str(datetime.timedelta(seconds=results_in_seconds[3][1]))],
                                   [str(datetime.timedelta(seconds=results_in_seconds[4][0])),
                                    str(datetime.timedelta(seconds=results_in_seconds[4][1]))],
                                   [str(datetime.timedelta(seconds=results_in_seconds[5][0])),
                                    str(datetime.timedelta(seconds=results_in_seconds[5][1]))],
                                   [str(datetime.timedelta(seconds=results_in_seconds[6][0])),
                                    str(datetime.timedelta(seconds=results_in_seconds[6][1]))]
                                   ]

        results_in_minutes = pd.DataFrame(
            results_in_minutes_list,
            columns=['lower bound', 'upper bound'],
            index=['1', '2', '3', '4', '5a', '5b', '5c']
        )

        results_in_minutes

if discipline == 'Bike':
    if 'Heart Rate' in testResults:
        hrBounds = st.sidebar.slider(
            'Select minimum and maximum heart rate [BPM]',
            0, 220, (50, 190))
        bikeTestAvgHR = st.sidebar.number_input('Input test average heart rate [BPM]', min_value=100, max_value=220,
                                               value=175, step=1)
        st.write(hrBikeZones(bikeTestAvgHR, hrBounds).df.style.format("{:.0f}"))
    if 'Power' in testResults:
        bikeTestAvgPower = st.sidebar.number_input('Input test average power [W]', min_value=50, max_value=2500,
                                                   value=200, step=1)
        st.write(powerBikeZones(bikeTestAvgPower).df.style.format("{:.0f}"))

if discipline == 'Swim':
    swimTestAvgPace = st.sidebar.text_input('Input test result for 1000 m [mm:ss]', value='20:00')
    swim_results_in_seconds = swimPaceZones(swimTestAvgPace).list

    swim_results_in_minutes_list = [[str(datetime.timedelta(seconds=swim_results_in_seconds[0][0])),
                                str(datetime.timedelta(seconds=swim_results_in_seconds[0][1]))],
                               [str(datetime.timedelta(seconds=swim_results_in_seconds[1][0])),
                                str(datetime.timedelta(seconds=swim_results_in_seconds[1][1]))],
                               [str(datetime.timedelta(seconds=swim_results_in_seconds[2][0])),
                                str(datetime.timedelta(seconds=swim_results_in_seconds[2][1]))],
                               [str(datetime.timedelta(seconds=swim_results_in_seconds[3][0])),
                                str(datetime.timedelta(seconds=swim_results_in_seconds[3][1]))],
                               [str(datetime.timedelta(seconds=swim_results_in_seconds[4][0])),
                                str(datetime.timedelta(seconds=swim_results_in_seconds[4][1]))],
                               [str(datetime.timedelta(seconds=swim_results_in_seconds[5][0])),
                                str(datetime.timedelta(seconds=swim_results_in_seconds[5][1]))],
                               [str(datetime.timedelta(seconds=swim_results_in_seconds[6][0])),
                                str(datetime.timedelta(seconds=swim_results_in_seconds[6][1]))]
                               ]

    swim_results_in_minutes = pd.DataFrame(
        swim_results_in_minutes_list,
        columns=['lower bound', 'upper bound'],
        index=['1', '2', '3', '4', '5a', '5b', '5c']
    )

    swim_results_in_minutes
