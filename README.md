
# trifacta

Trifacta client that makes it easy to integrate Trifacta into your production and data science workflows

### Usage Scenarios
- **Jupyter**: Invoke Trifacta jobs from a Jupyter notebook and pass data back and forth between Jupyter and Trifacta
- **Other Notebooks**: Integrate Trifacta with Azure Databricks, Zepellin or any other notebook-style interface that supports Python
- **Scripts**: Automate Trifacta jobs and input/output using python scripts that can be easily executed from the command line or called from an external scheduler

### Functionality
This library makes it simple to do the following:
1. Connect to a Trifacta instance
2. Run a job
3. Download results to a pandas dataframe OR Download results as text/csv
4. Upload files to Trifacta

Note that file uploads and downloads are performed using httpfs, and require that port 14000 be opened on the Trifacta server


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
#Step 3a: Get a pandas dataframe with the results
df = t.get_dataframe('/trifacta/queryResults/demo@trifacta.com/demo_output.csv')
```


```python
df
```




<div>
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
#Step 3b: Download results as text/csv
file_contents = t.get_file_contents('/trifacta/queryResults/demo@trifacta.com/demo_output.csv')
with open('demo_output.csv', 'w') as f:
    f.write(file_contents)
```


```python
#Show the first few rows of the CSV file
!head demo_output.csv
```

    "Neighborhood","HouseStyle","row_count","sum_LotArea"
    "NAmes","1Story","159","1589811"
    "CollgCr","1Story","91","841644"
    "Gilbert","2Story","60","668112"
    "Timber","1Story","23","554694"
    "CollgCr","2Story","53","546602"
    "NridgHt","1Story","51","537687"
    "Sawyer","1Story","53","528438"
    "Edwards","1Story","53","511296"
    "NoRidge","2Story","33","485691"



```python
#Step 4: Upload files to Trifacta
t.put_file_contents('/trifacta/uploads/demo_output.csv', file_contents)
```




    True


