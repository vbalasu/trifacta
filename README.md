
# trifacta

Use this library to do the following:
1. Connect to a Trifacta instance
2. Run a job
3. Download results to a pandas dataframe; OR
4. Download results as text/csv


```python
#!pip install trifacta
import trifacta
```


```python
#Step 1: Connect to Trifacta by providing the URL, username and password
t = trifacta.Client('https://partnerdemo.trifacta.net', 'demo@trifacta.com', 'demo')
```

#### Get the wrangled dataset id from the URL in the Trifacta UI
Make sure that you have run the job manually at least once
![Screenshot_recipe](https://cdn.rawgit.com/vbalasu/trifacta/86890c1f/screenshot_recipe.png)

#### Note the output path (be sure to set it to "replace")
![Run Job](https://cdn.rawgit.com/vbalasu/trifacta/86890c1f/run_job_highlight.png)


```python
#Step 2: Run the job
t.run_job(14478)
```

    About to run job
    {'jobgroupId': 3926, 'jobIds': [7513, 7514], 'reason': 'JobStarted', 'sessionId': 'b9d327f0-8e19-11e8-8feb-9fabf204e996'}
    2018-07-22 18:43:01.427594 InProgress
    2018-07-22 18:43:06.791576 Complete





    True




```python
#Step 3: Get a pandas dataframe with the results
df = t.get_dataframe('/trifacta/queryResults/demo@trifacta.com/demo_output.csv')
```


```python
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood</th>
      <th>HouseStyle</th>
      <th>row_count</th>
      <th>sum_LotArea</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NAmes</td>
      <td>1Story</td>
      <td>159</td>
      <td>1589811</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CollgCr</td>
      <td>1Story</td>
      <td>91</td>
      <td>841644</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Gilbert</td>
      <td>2Story</td>
      <td>60</td>
      <td>668112</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Timber</td>
      <td>1Story</td>
      <td>23</td>
      <td>554694</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CollgCr</td>
      <td>2Story</td>
      <td>53</td>
      <td>546602</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NridgHt</td>
      <td>1Story</td>
      <td>51</td>
      <td>537687</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Sawyer</td>
      <td>1Story</td>
      <td>53</td>
      <td>528438</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Edwards</td>
      <td>1Story</td>
      <td>53</td>
      <td>511296</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NoRidge</td>
      <td>2Story</td>
      <td>33</td>
      <td>485691</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NWAmes</td>
      <td>1Story</td>
      <td>35</td>
      <td>403813</td>
    </tr>
    <tr>
      <th>10</th>
      <td>ClearCr</td>
      <td>1Story</td>
      <td>11</td>
      <td>395797</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Mitchel</td>
      <td>1Story</td>
      <td>32</td>
      <td>394436</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Somerst</td>
      <td>1Story</td>
      <td>37</td>
      <td>350820</td>
    </tr>
    <tr>
      <th>13</th>
      <td>NWAmes</td>
      <td>2Story</td>
      <td>29</td>
      <td>348885</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Somerst</td>
      <td>2Story</td>
      <td>49</td>
      <td>323495</td>
    </tr>
    <tr>
      <th>15</th>
      <td>NridgHt</td>
      <td>2Story</td>
      <td>26</td>
      <td>300685</td>
    </tr>
    <tr>
      <th>16</th>
      <td>OldTown</td>
      <td>2Story</td>
      <td>32</td>
      <td>274465</td>
    </tr>
    <tr>
      <th>17</th>
      <td>SawyerW</td>
      <td>1Story</td>
      <td>28</td>
      <td>271008</td>
    </tr>
    <tr>
      <th>18</th>
      <td>OldTown</td>
      <td>1.5Fin</td>
      <td>33</td>
      <td>267283</td>
    </tr>
    <tr>
      <th>19</th>
      <td>ClearCr</td>
      <td>1.5Fin</td>
      <td>6</td>
      <td>266593</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Crawfor</td>
      <td>1Story</td>
      <td>19</td>
      <td>260639</td>
    </tr>
    <tr>
      <th>21</th>
      <td>SawyerW</td>
      <td>2Story</td>
      <td>25</td>
      <td>255102</td>
    </tr>
    <tr>
      <th>22</th>
      <td>NAmes</td>
      <td>2Story</td>
      <td>22</td>
      <td>249793</td>
    </tr>
    <tr>
      <th>23</th>
      <td>OldTown</td>
      <td>1Story</td>
      <td>33</td>
      <td>240257</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Edwards</td>
      <td>1.5Fin</td>
      <td>22</td>
      <td>228970</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Crawfor</td>
      <td>2Story</td>
      <td>20</td>
      <td>222029</td>
    </tr>
    <tr>
      <th>26</th>
      <td>NAmes</td>
      <td>SLvl</td>
      <td>21</td>
      <td>221177</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Edwards</td>
      <td>2Story</td>
      <td>14</td>
      <td>185799</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Timber</td>
      <td>1.5Fin</td>
      <td>2</td>
      <td>178418</td>
    </tr>
    <tr>
      <th>29</th>
      <td>BrkSide</td>
      <td>1.5Fin</td>
      <td>25</td>
      <td>172233</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>66</th>
      <td>CollgCr</td>
      <td>SLvl</td>
      <td>3</td>
      <td>30135</td>
    </tr>
    <tr>
      <th>67</th>
      <td>BrDale</td>
      <td>2Story</td>
      <td>16</td>
      <td>28816</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Veenker</td>
      <td>SLvl</td>
      <td>2</td>
      <td>25757</td>
    </tr>
    <tr>
      <th>69</th>
      <td>NoRidge</td>
      <td>1.5Fin</td>
      <td>2</td>
      <td>25398</td>
    </tr>
    <tr>
      <th>70</th>
      <td>SawyerW</td>
      <td>SFoyer</td>
      <td>3</td>
      <td>25267</td>
    </tr>
    <tr>
      <th>71</th>
      <td>CollgCr</td>
      <td>SFoyer</td>
      <td>3</td>
      <td>24491</td>
    </tr>
    <tr>
      <th>72</th>
      <td>MeadowV</td>
      <td>2Story</td>
      <td>8</td>
      <td>19611</td>
    </tr>
    <tr>
      <th>73</th>
      <td>NPkVill</td>
      <td>1Story</td>
      <td>4</td>
      <td>17942</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Veenker</td>
      <td>2Story</td>
      <td>1</td>
      <td>17542</td>
    </tr>
    <tr>
      <th>75</th>
      <td>NAmes</td>
      <td>1.5Unf</td>
      <td>2</td>
      <td>16827</td>
    </tr>
    <tr>
      <th>76</th>
      <td>SWISU</td>
      <td>1Story</td>
      <td>2</td>
      <td>14692</td>
    </tr>
    <tr>
      <th>77</th>
      <td>OldTown</td>
      <td>SFoyer</td>
      <td>2</td>
      <td>14179</td>
    </tr>
    <tr>
      <th>78</th>
      <td>NWAmes</td>
      <td>1.5Fin</td>
      <td>1</td>
      <td>13837</td>
    </tr>
    <tr>
      <th>79</th>
      <td>SawyerW</td>
      <td>SLvl</td>
      <td>1</td>
      <td>12800</td>
    </tr>
    <tr>
      <th>80</th>
      <td>IDOTRR</td>
      <td>1.5Unf</td>
      <td>2</td>
      <td>12449</td>
    </tr>
    <tr>
      <th>81</th>
      <td>SawyerW</td>
      <td>1.5Fin</td>
      <td>1</td>
      <td>12327</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Gilbert</td>
      <td>1.5Fin</td>
      <td>1</td>
      <td>12134</td>
    </tr>
    <tr>
      <th>83</th>
      <td>BrkSide</td>
      <td>2.5Unf</td>
      <td>1</td>
      <td>11888</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Crawfor</td>
      <td>2.5Fin</td>
      <td>1</td>
      <td>11526</td>
    </tr>
    <tr>
      <th>85</th>
      <td>NPkVill</td>
      <td>2Story</td>
      <td>5</td>
      <td>11465</td>
    </tr>
    <tr>
      <th>86</th>
      <td>NWAmes</td>
      <td>SFoyer</td>
      <td>1</td>
      <td>10625</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Crawfor</td>
      <td>1.5Unf</td>
      <td>1</td>
      <td>10594</td>
    </tr>
    <tr>
      <th>88</th>
      <td>OldTown</td>
      <td>1.5Unf</td>
      <td>2</td>
      <td>9888</td>
    </tr>
    <tr>
      <th>89</th>
      <td>MeadowV</td>
      <td>SFoyer</td>
      <td>6</td>
      <td>9853</td>
    </tr>
    <tr>
      <th>90</th>
      <td>SawyerW</td>
      <td>1.5Unf</td>
      <td>1</td>
      <td>9000</td>
    </tr>
    <tr>
      <th>91</th>
      <td>MeadowV</td>
      <td>1Story</td>
      <td>2</td>
      <td>8448</td>
    </tr>
    <tr>
      <th>92</th>
      <td>IDOTRR</td>
      <td>2.5Unf</td>
      <td>1</td>
      <td>7200</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Crawfor</td>
      <td>2.5Unf</td>
      <td>1</td>
      <td>7128</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Blueste</td>
      <td>2Story</td>
      <td>2</td>
      <td>3250</td>
    </tr>
    <tr>
      <th>95</th>
      <td>MeadowV</td>
      <td>SLvl</td>
      <td>1</td>
      <td>1596</td>
    </tr>
  </tbody>
</table>
<p>96 rows × 4 columns</p>
</div>




```python
#Step 4: Download results as text/csv
file_contents = t.get_file_contents('/trifacta/queryResults/demo@trifacta.com/demo_output.csv')
```


```python
file_contents
```




    '"Neighborhood","HouseStyle","row_count","sum_LotArea"\n"NAmes","1Story","159","1589811"\n"CollgCr","1Story","91","841644"\n"Gilbert","2Story","60","668112"\n"Timber","1Story","23","554694"\n"CollgCr","2Story","53","546602"\n"NridgHt","1Story","51","537687"\n"Sawyer","1Story","53","528438"\n"Edwards","1Story","53","511296"\n"NoRidge","2Story","33","485691"\n"NWAmes","1Story","35","403813"\n"ClearCr","1Story","11","395797"\n"Mitchel","1Story","32","394436"\n"Somerst","1Story","37","350820"\n"NWAmes","2Story","29","348885"\n"Somerst","2Story","49","323495"\n"NridgHt","2Story","26","300685"\n"OldTown","2Story","32","274465"\n"SawyerW","1Story","28","271008"\n"OldTown","1.5Fin","33","267283"\n"ClearCr","1.5Fin","6","266593"\n"Crawfor","1Story","19","260639"\n"SawyerW","2Story","25","255102"\n"NAmes","2Story","22","249793"\n"OldTown","1Story","33","240257"\n"Edwards","1.5Fin","22","228970"\n"Crawfor","2Story","20","222029"\n"NAmes","SLvl","21","221177"\n"Edwards","2Story","14","185799"\n"Timber","1.5Fin","2","178418"\n"BrkSide","1.5Fin","25","172233"\n"ClearCr","2Story","8","164932"\n"Gilbert","1Story","11","155214"\n"NAmes","1.5Fin","15","153818"\n"StoneBr","1Story","18","149552"\n"BrkSide","1Story","20","134561"\n"IDOTRR","1.5Fin","16","133246"\n"Veenker","1Story","8","128367"\n"Timber","2Story","9","122229"\n"StoneBr","2Story","7","117246"\n"IDOTRR","1Story","13","109070"\n"Crawfor","1.5Fin","9","90378"\n"SWISU","1.5Fin","12","89785"\n"NWAmes","SLvl","7","86695"\n"OldTown","2.5Unf","8","74470"\n"NoRidge","1Story","6","71886"\n"Sawyer","1.5Fin","5","69098"\n"BrkSide","2Story","6","67318"\n"Sawyer","SFoyer","6","65721"\n"Gilbert","SLvl","7","63493"\n"Blmngtn","1Story","17","57769"\n"SWISU","2Story","7","57349"\n"Sawyer","SLvl","5","57205"\n"Edwards","SLvl","6","53571"\n"Sawyer","2Story","5","53525"\n"Mitchel","SLvl","5","51425"\n"NAmes","SFoyer","6","50055"\n"Mitchel","1.5Fin","4","49570"\n"OldTown","2.5Fin","3","46856"\n"Timber","SLvl","4","43900"\n"Edwards","SFoyer","5","42229"\n"Mitchel","SFoyer","5","41475"\n"SWISU","2.5Fin","4","41363"\n"BrkSide","1.5Unf","6","40904"\n"IDOTRR","2Story","5","38074"\n"ClearCr","SLvl","3","37199"\n"Mitchel","2Story","3","32684"\n"CollgCr","SLvl","3","30135"\n"BrDale","2Story","16","28816"\n"Veenker","SLvl","2","25757"\n"NoRidge","1.5Fin","2","25398"\n"SawyerW","SFoyer","3","25267"\n"CollgCr","SFoyer","3","24491"\n"MeadowV","2Story","8","19611"\n"NPkVill","1Story","4","17942"\n"Veenker","2Story","1","17542"\n"NAmes","1.5Unf","2","16827"\n"SWISU","1Story","2","14692"\n"OldTown","SFoyer","2","14179"\n"NWAmes","1.5Fin","1","13837"\n"SawyerW","SLvl","1","12800"\n"IDOTRR","1.5Unf","2","12449"\n"SawyerW","1.5Fin","1","12327"\n"Gilbert","1.5Fin","1","12134"\n"BrkSide","2.5Unf","1","11888"\n"Crawfor","2.5Fin","1","11526"\n"NPkVill","2Story","5","11465"\n"NWAmes","SFoyer","1","10625"\n"Crawfor","1.5Unf","1","10594"\n"OldTown","1.5Unf","2","9888"\n"MeadowV","SFoyer","6","9853"\n"SawyerW","1.5Unf","1","9000"\n"MeadowV","1Story","2","8448"\n"IDOTRR","2.5Unf","1","7200"\n"Crawfor","2.5Unf","1","7128"\n"Blueste","2Story","2","3250"\n"MeadowV","SLvl","1","1596"\n'


