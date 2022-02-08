from calendar import c
from flask import Flask, render_template, request, url_for
import pandas as pd
import numpy as np
import math

data = [['Evan Krikler', 'Over', 'Super Bowl', 'Over', 'Andy Reid', 'Over', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Touchdown', 'Gronk', 'Kelce', 'Bucs', 'Chiefs', 'Butker', 'Mahomes', 'Bucs', 'Brady', 'Jones', 'No', 'No', 'Kelce', 'CEH', 'Over', 'Under', 'Over', 'Over', 'Jones', 'Pringle', 'Over', 'Over', 'Yes', 'Chiefs', 'Chiefs', 'Bucs', 'Mahomes', 'Over', 'Blue', 'Blinding Lights', 'Yes', 'God', 'Chiefs 35-21'],
['Carrie Glass', 'Over', 'Super Bowl', 'Over', 'Bruce Arians', 'Under', 'Yes', 'Heads', 'Bucs', 'Pass', 'Field Goal', 'Evans', 'Williams', 'Chiefs', 'Chiefs', 'Butker', 'Mahomes', 'Bucs', 'Mahomes', 'Edwards', 'No', 'No', 'Kelce', 'Fournette', 'Under', 'Over', 'Under', 'Under', 'Jones', 'Godwin', 'Over', 'Under', 'No', 'Chiefs', 'Chiefs', 'Chiefs', 'Mahomes', 'Under', 'Orange', 'Acquainted', 'No', 'Teammates', 'KC 30 TB 24'],
['Dan segal', 'Over', 'Super Bowl', 'Under', 'Andy Reid', 'Over', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Touchdown', 'Kelce', 'Evans', 'Chiefs', 'Bucs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Breeland ', 'No', 'No', 'Godwin', 'CEH', 'Under', 'Under', 'Under', 'Under', 'Suh', 'Kelce', 'Under', 'Over', 'No', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Under', 'Blue', 'Blinding Lights', 'No', 'Teammates', 'Chiefs 28-21'],
['yoni Gootgarts ', 'Under', 'Super Bowl', 'Under', 'Andy Reid', 'Over', 'No', 'Heads', 'Bucs', 'Pass', 'Touchdown', 'Evans', 'Kelce', 'Bucs', 'Chiefs', 'Butker', 'Mahomes', 'Chiefs', 'Fournette', 'Mathieu', 'No', 'No', 'Hill', 'Fournette', 'Over', 'Under', 'Under', 'Over', 'Clark', 'Brown', 'Over', 'Under', 'Yes', 'Bucs', 'Bucs', 'Bucs', 'Mahomes', 'Over', 'Blue', 'Blinding Lights', 'Yes', 'God', 'Chiefs, 31-27'],
['Shaboyroy', 'Under', 'Super Bowl', 'Over', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Chiefs', 'Run', 'Touchdown', 'CEH', 'Evans', 'Chiefs', 'Bucs', 'Butker', 'Mahomes', 'Bucs', 'Brady', 'Jones', 'No', 'No', 'Hill', 'Fournette', 'Over', 'Over', 'Over', 'Over', 'Jones', 'Kelce', 'Over', 'Under', 'Yes', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Over', 'Blue', 'Blinding Lights', 'No', 'Family', 'Cheifs, 35-27'],
['Danny G', 'Over', 'Super Bowl', 'Over', 'Andy Reid', 'Over', 'Yes', 'Tails', 'Chiefs', 'Run', 'Touchdown', 'Kelce', 'Williams', 'Chiefs', 'Bucs', 'Succop', 'Mahomes', 'Chiefs', 'Jones', 'Sorensen', 'No', 'No', 'Kelce', 'Fournette', 'Under', 'Over', 'Under', 'Over', 'Suh', 'Kelce', 'Under', 'Over', 'Yes', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Over', 'Orange', 'Blinding Lights', 'Yes', 'God', 'KC 27-19'],
['Gabe', 'Over', 'Super Bowl', 'Over', 'Andy Reid', 'Under', 'Yes', 'Heads', 'Bucs', 'Pass', 'Touchdown', 'Fournette', 'Godwin', 'Bucs', 'Bucs', 'Succop', 'Mahomes', 'Bucs', 'CEH', 'David', 'No', 'Yes', 'Godwin', 'Fournette', 'Over', 'Under', 'Under', 'Over', 'Clark', 'Watkins', 'Under', 'Over', 'Yes', 'Chiefs', 'Chiefs', 'Bucs', 'Mahomes', 'Over', 'Orange', 'Blinding Lights', 'Yes', 'Teammates', '31-27 Chiefs win'],
['Daniel Tyberg', 'Over', 'Super Bowl', 'Under', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Field Goal', 'Kelce', 'Evans ', 'Bucs', 'Bucs', 'Butker', 'Mahomes', 'Bucs', 'Mahomes', 'Bunting', 'No', 'No', 'Hill', 'Fournette', 'Over', 'Over', 'Under', 'Over', 'Barrett', 'Brate', 'Under', 'Over', 'No', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Over', 'Orange', 'Blinding Lights', 'Yes', 'God', 'Chiefs, 33-30'],
['Chad Pollack', 'Over', 'Age', 'Under', 'Andy Reid', 'Under', 'Yes', 'Heads', 'Chiefs', 'Run', 'Touchdown', 'Kelce', 'Hill', 'Chiefs', 'Chiefs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Mathieu', 'No', 'No', 'Kelce', 'Fournette', 'Under', 'Under', 'Under', 'Under', 'Clark', 'Kelce', 'Under', 'Over', 'No', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Over', 'Orange', 'Blinding Lights', 'No', 'Teammates', 'Chiefs 30-27'],
['Sammy Zucker', 'Over', 'Super Bowl', 'Over', 'Andy Reid', 'Over', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Touchdown', 'Kelce', 'Godwin', 'Chiefs', 'Bucs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Sneed', 'No', 'No', 'Hill', 'Fournette', 'Under', 'Over', 'Under', 'Over', 'JPP', 'Kelce', 'Under', 'Over', 'Yes', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Under', 'Orange', 'Blinding Lights', 'No', 'Teammates', 'Chiefs and 30-26'],
['Postelnik', 'Over', 'Super Bowl', 'Over', 'Andy Reid', 'Under', 'Yes', 'Heads', 'Bucs', 'Pass', 'Touchdown', 'Kelce', 'Gronk', 'Chiefs', 'Chiefs', 'Succop', 'Mahomes', 'Bucs', 'Evans', 'Jones', 'No', 'No', 'Hill', 'CEH', 'Under', 'Over', 'Over', 'Over', 'Barrett', 'Kelce', 'Over', 'Over', 'Yes', 'Chiefs', 'Bucs', 'Chiefs', 'Mahomes', 'Under', 'Red', 'Blinding Lights', 'No', 'Family', 'Chiefs, 63'],
['Jason Tapiero', 'Under', 'Super Bowl', 'Under', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Field Goal', 'Kelce', 'Evans', 'Chiefs', 'Bucs', 'Succop', 'Mahomes', 'Bucs', 'Brady', 'Mathieu', 'No', 'No', 'Kelce', 'Fournette', 'Under', 'Over', 'Under', 'Under', 'Jones', 'Godwin', 'Over', 'Under', 'No', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Under', 'Yellow', 'Blinding Lights', 'No', 'God', 'Chiefs 27-20'],
['Max Ashley', 'Over', 'Age', 'Under', 'Andy Reid', 'Over', 'Yes', 'Heads', 'Bucs', 'Run', 'Touchdown', 'Fournette ', 'Kelce ', 'Bucs', 'Chiefs', 'Succop', 'Mahomes', 'Chiefs', 'Brady ', 'Matthieu ', 'No', 'No', 'Kelce', 'Fournette', 'Under', 'Under', 'Under', 'Over', 'Barrett ', 'Godwin ', 'Under', 'Under', 'No', 'Chiefs', 'Chiefs', 'Bucs', 'Mahomes', 'Under', 'Purple ', 'Blinding Lights', 'No', 'Family', 'Chiefs 31-24'],
['Ryan Erdman', 'Over', 'Super Bowl', 'Over', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Field Goal', 'Kelce', 'CEH', 'Bucs', 'Chiefs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Sorensen', 'No', 'No', 'Kelce', 'Jones', 'Over', 'Under', 'Under', 'Over', 'JPP', 'Godwin', 'Under', 'Over', 'Yes', 'Chiefs', 'Chiefs', 'Bucs', 'Mahomes', 'Over', 'Yellow ', 'Blinding Lights', 'No', 'God', 'Chiefs 34 Bucks 24 '],
['Joe m', 'Under', 'Super Bowl', 'Over', 'Andy Reid', 'Under', 'Yes', 'Heads', 'Bucs', 'Pass', 'Touchdown', 'Godwin', 'Kelce', 'Bucs', 'Bucs', 'Succop', 'Brady', 'Bucs', 'Mahomes', 'Sorensen', 'Yes', 'Yes', 'Hill', 'Jones', 'Under', 'Over', 'Over', 'Over', 'Jones', 'Gronk ', 'Under', 'Over', 'No', 'Chiefs', 'Bucs', 'Bucs', 'Brady', 'Over', 'White', "Can't feel my face", 'No', 'Family', 'TB, 34-28'],
['Benji & Coach Dave Bloom', 'Over', 'Super Bowl', 'Over', 'Andy Reid', 'Over', 'Yes', 'Heads', 'Chiefs', 'Pass', 'Touchdown', 'Kelce', 'Fournette', 'Chiefs', 'Bucs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Hitchens', 'No', 'Yes', 'Kelce', 'Fournette', 'Over', 'Over', 'Under', 'Over', 'Barrett', 'Evans', 'Over', 'Under', 'No', 'Chiefs', 'Bucs', 'Chiefs', 'Brady', 'Under', 'Orange', 'Heartless', 'No', 'Family', 'KC 30-26'],
['Robbie Raskin', 'Over', 'Super Bowl', 'Under', 'Andy Reid', 'Under', 'Yes', 'Heads', 'Bucs', 'Run', 'Touchdown', 'Gronk', 'Godwin', 'Bucs', 'Bucs', 'Succop', 'Mahomes', 'Bucs', 'CEH', 'White', 'No', 'No', 'Hill', 'Fournette', 'Under', 'Under', 'Under', 'Under', 'JPP', 'Evans', 'Over', 'Under', 'No', 'Bucs', 'Chiefs', 'Bucs', 'Brady', 'Over', 'Yellow', "Can't feel my face", 'No', 'Teammates', 'Bucs, 31-28'],
['Audrey Slater', 'Over', 'Super Bowl', 'Under', 'Bruce Arians', 'Under', 'Yes', 'Heads', 'Chiefs', 'Pass', 'Field Goal', 'Mahomes', 'Fournette', 'Bucs', 'Chiefs', 'Succop', 'Mahomes', 'Chiefs', 'Mahomes', 'Davis', 'No', 'No', 'Godwin', 'Fournette', 'Over', 'Under', 'Over', 'Under', 'JPP', 'Gronk', 'Over', 'Under', 'Yes', 'Bucs', 'Bucs', 'Chiefs', 'Mahomes', 'Over', 'Blue', 'I feel it coming', 'No', 'Teammates', 'KC 32 TB 26'],
['Nadav Amar', 'Under', 'Super Bowl', 'Under', 'Andy Reid', 'Under', 'Yes', 'Heads', 'Chiefs', 'Run', 'Touchdown', 'CEH', 'Kelce', 'Chiefs', 'Chiefs', 'Butker', 'Mahomes', 'Bucs', 'Mahomes ', 'Barrett', 'No', 'No', 'Hill', 'CEH', 'Under', 'Over', 'Under', 'Under', 'Jones', 'Kelce', 'Over', 'Under', 'No', 'Chiefs', 'Bucs', 'Chiefs', 'Mahomes', 'Over', 'Red', 'I feel it coming ', 'No', 'Teammates', 'Chiefs 31-27'],
['Adam Sabba', 'Over', 'Super Bowl', 'Over', 'Andy Reid', 'Under', 'Yes', 'Heads', 'Bucs', 'Run', 'Field Goal', 'Evans', 'Kelce', 'Bucs', 'Chiefs', 'Succop', 'Mahomes', 'Chiefs', 'Mahomes', 'Mathieu', 'No', 'No', 'Hill', 'Jones', 'Over', 'Over', 'Under', 'Under', 'White', 'Kelce', 'Over', 'Over', 'No', 'Bucs', 'Chiefs', 'Bucs', 'Mahomes', 'Under', 'Orange', 'In Your Eyes', 'No', 'God', 'Chiefs 33-24'],
['Daniel Shuman', 'Over', 'Age', 'Under', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Bucs', 'Pass', 'Touchdown', 'Hardman', 'Evans', 'Chiefs', 'Bucs', 'Butker', 'Mahomes', 'Bucs', 'Mahomes', 'White', 'No', 'No', 'Kelce', 'Fournette', 'Under', 'Under', 'Under', 'Over', 'White', 'Kelce', 'Under', 'Over', 'No', 'Chiefs', 'Chiefs', 'Bucs', 'Mahomes', 'Under', 'Orange', 'Pray for Me', 'No', 'Teammates', 'Chiefs win 30-24'],
['Ophir Dzaldov', 'Under', 'Super Bowl', 'Over', 'Andy Reid', 'Over', 'Yes', 'Heads', 'Chiefs', 'Pass', 'Touchdown', 'Kelce', 'Kelce', 'Chiefs', 'Chiefs', 'Butker', 'Mahomes', 'Chiefs', 'Brady', 'Mathieu ', 'No', 'Yes', 'Kelce', 'Fournette', 'Over', 'Over', 'Over', 'Under', 'Sneed', 'Kelce', 'Over', 'Over', 'Yes', 'Chiefs', 'Chiefs', 'Chiefs', 'Mahomes', 'Over', 'Orange', 'Save your tears', 'No', 'Teammates', 'KC 37 24'],
['Jamie DeRosen', 'Over', 'Super Bowl', 'Under', 'Andy Reid', 'Over', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Touchdown', 'Mahomes', 'Kelce ', 'Chiefs', 'Chiefs', 'Succop', 'Mahomes', 'Chiefs', 'Brady ', 'Mathieu', 'No', 'Yes', 'Hill', 'Fournette', 'Under', 'Over', 'Over', 'Over', 'Suh', 'Kelce', 'Under', 'Under', 'Yes', 'Chiefs', 'Bucs', 'Chiefs', 'Mahomes', 'Over', 'Orange', 'Save Your Tears', 'No', 'Teammates', 'Chiefs or the Leafs, 38 - 27'],
['Jack Quags', 'Over', 'Age', 'Under', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Field Goal', 'Fournette ', 'Hardman', 'Bucs', 'Chiefs', 'Succop', 'Mahomes', 'Bucs', 'Williams', 'White', 'No', 'No', 'Kelce', 'Fournette', 'Over', 'Over', 'Under', 'Over', 'Clark', 'Brown ', 'Under', 'Over', 'Yes', 'Bucs', 'Bucs', 'Chiefs', 'Brady', 'Over', 'Orange', 'Star Boy', 'No', 'Teammates', 'Bucs, 35-32'],
['Daniel bleiwas', 'Over', 'Super Bowl', 'Under', 'Andy Reid', 'Over', 'Yes', 'Heads', 'Chiefs', 'Run', 'Touchdown', 'Evans', 'Kelce', 'Bucs', 'Chiefs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Mathieu', 'No', 'No', 'Kelce', 'Fournette', 'Under', 'Under', 'Under', 'Over', 'Jones', 'Godwin', 'Under', 'Over', 'Yes', 'Bucs', 'Bucs', 'Bucs', 'Mahomes', 'Over', 'None', 'Star Boy', 'No', 'Teammates', 'Mahomes 35-32'],
['Jake Raubvogel', 'Over', 'Age', 'Under', 'Bruce Arians', 'Under', 'Yes', 'Heads', 'Chiefs', 'Run', 'Touchdown', 'Kelce', 'Hill', 'Chiefs', 'Bucs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Mathieu', 'No', 'No', 'Kelce', 'Fournette', 'Under', 'Over', 'Under', 'Under', 'JPP', 'Godwin', 'Over', 'Under', 'No', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Over', 'Orange', 'Star Boy', 'No', 'Teammates', 'KC 31-28'],
['Noah Chaikof (ChaikDirty)', 'Over', 'Age', 'Under', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Bucs', 'Run', 'Touchdown', 'Hardmen', 'Evans', 'Chiefs', 'Bucs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Mathieu', 'No', 'No', 'Kelce', 'Fournette', 'Under', 'Over', 'Under', 'Under', 'Jones', 'Hill', 'Over', 'Under', 'No', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Under', 'Orange', 'Star Boy', 'No', 'Teammates', 'Chiefs, 31-24'],
['Jake Engel', 'Over', 'Age', 'Over', 'Andy Reid', 'Over', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Touchdown', 'Hill', 'Kelce', 'Chiefs', 'Chiefs', 'Succop', 'Mahomes', 'Bucs', 'Robinson', 'White', 'No', 'No', 'Hill', 'Fournette', 'Under', 'Under', 'Under', 'Over', 'Clark', 'Evans', 'Under', 'Under', 'Yes', 'Chiefs', 'Chiefs', 'Bucs', 'Mahomes', 'Over', 'Orange', 'Star Boy', 'No', 'Teammates', '38-24 (Chiefs)'],
['Omri', 'Over', 'Super Bowl', 'Under', 'Andy Reid', 'Over', 'Yes', 'Tails', 'Chiefs', 'Run', 'Touchdown', 'Kelce', 'Godwin', 'Chiefs', 'Bucs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Breeland', 'No', 'No', 'Hill', 'Fournette', 'Over', 'Under', 'Under', 'Over', 'Barrett', 'Godwin', 'Under', 'Under', 'No', 'Chiefs', 'Bucs', 'Chiefs', 'Mahomes', 'Over', 'Orange', 'Star Boy', 'No', 'Teammates', 'Chiefs 38-24'],
['Shayne Friedman', 'Over', 'Age', 'Under', 'Andy Reid', 'Under', 'Yes', 'Heads', 'Bucs', 'Run', 'Touchdown', 'Evans', 'Fournette', 'Bucs', 'Bucs', 'Succop', 'Mahomes', 'Chiefs', 'Mahomes', 'Winfield Jr.', 'No', 'No', 'Kelce', 'Fournette', 'Over', 'Under', 'Under', 'Over', 'Barrett', 'Godwin', 'Over', 'Under', 'Yes', 'Chiefs', 'Bucs', 'Chiefs', 'Brady', 'Over', 'Orange', 'Star Boy', 'No', 'Teammates', 'Bucs 34-31'],
['Ryan Orelowitz', 'Under', 'Super Bowl', 'Under', 'Andy Reid', 'Over', 'Yes', 'Heads', 'Chiefs', 'Run', 'Field Goal', 'Hill', 'Kelce', 'Chiefs', 'Chiefs', 'Butker', 'Mahomes', 'Chiefs', 'Godwin', 'Mathieu', 'No', 'No', 'Kelce', 'Jones', 'Under', 'Under', 'Over', 'Under', 'Harris', 'Godwin', 'Over', 'Under', 'Yes', 'Bucs', 'Chiefs', 'Bucs', 'Mahomes', 'Over', 'Red', 'Star Boy', 'No', 'Teammates', 'Chiefs 34-28'],
['Josh Sinclair', 'Under', 'Super Bowl', 'Over', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Bucs', 'Run', 'Touchdown', 'Hill', 'Evans', 'Chiefs', 'Bucs', 'Succop', 'Mahomes', 'Bucs', 'Brady', 'Mathieu', 'No', 'No', 'Hill', 'Fournette', 'Under', 'Over', 'Under', 'Under', 'Jones', 'Kelce', 'Under', 'Under', 'Yes', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Over', 'Red', 'Star Boy', 'No', 'Teammates', '34-24 KC'],
['Dr. Integrity', 'Over', 'Super Bowl', 'Under', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Bucs', 'Pass', 'Touchdown', 'Kelce', 'Kelce', 'Chiefs', 'Chiefs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Mathieu', 'No', 'No', 'Hill', 'Fournette', 'Over', 'Under', 'Under', 'Under', 'Barrett', 'Kelce', 'Over', 'Under', 'No', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Under', 'Red', 'Star Boy', 'No', 'Teammates', 'Chiefs 31-21'],
['Adam Gropper', 'Under', 'Super Bowl', 'Under', 'Andy Reid', 'Over', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Touchdown', 'Kelce', 'Kelce', 'Chiefs', 'Chiefs', 'Butker', 'Mahomes', 'Chiefs', 'Brady', 'Mathieu', 'No', 'No', 'Kelce ', 'Fournette', 'Under', 'Over', 'Under', 'Under', 'Clark', 'Kelce', 'Under', 'Under', 'Yes', 'Chiefs', 'Chiefs', 'Bucs', 'Mahomes', 'Over', 'Red', 'Star Boy', 'No', 'God', 'Chiefs  31-24 '],
['Robbie Middlestadt', 'Over', 'Super Bowl', 'Over', 'Andy Reid', 'Over', 'Yes', 'Heads', 'Chiefs', 'Pass', 'Touchdown', 'Mahomes', 'Kelce', 'Chiefs', 'Chiefs', 'Succop', 'Mahomes', 'Chiefs', 'Brady', 'Sorensen', 'No', 'No', 'Godwin', 'CEH', 'Under', 'Under', 'Over', 'Under', 'JPP', 'Williams', 'Over', 'Over', 'Yes', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Under', 'Red', 'Star Boy', 'Yes', 'Teammates', 'Chiefs, 29-23'],
['Rena and Jared', 'Over', 'Super Bowl', 'Under', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Chiefs', 'Run', 'Touchdown', 'Kelce ', 'Gronk', 'Bucs', 'Bucs', 'Succop', 'Mahomes', 'Chiefs', 'Mahomes', 'Davis', 'No', 'No', 'Hill', 'Fournette', 'Over', 'Under', 'Under', 'Over', 'Barrett', 'Evans', 'Over', 'Under', 'Yes', 'Bucs', 'Bucs', 'Bucs', 'Brady', 'Under', 'Red', 'Star Boy', 'No', 'Teammates', 'Bucs  28-24'],
['Sammy Raskin', 'Over', 'Super Bowl', 'Over', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Bucs', 'Run', 'Touchdown', 'Kelce', 'Evans', 'Chiefs', 'Bucs', 'Butker', 'Mahomes', 'Chiefs', 'Brady', 'Mathieu', 'No', 'No', 'Hill', 'Williams', 'Under', 'Under', 'Under', 'Under', 'Clark', 'Kelce', 'Under', 'Under', 'No', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Under', 'Red', 'The Hills', 'No', 'Teammates', 'KC 34 TB 22'],
['Ryan Kirshenbaum', 'Over', 'Super Bowl', 'Under', 'Andy Reid', 'Under', 'No', 'Heads', 'Chiefs', 'Pass', 'Touchdown', 'Kelce ', 'Evans', 'Chiefs', 'Bucs', 'Butker', 'Mahomes', 'Chiefs', 'Brady', 'Mathieu', 'No', 'No', 'Hill', 'Bell', 'Under', 'Over', 'Under', 'Under', 'White', 'Bell', 'Over', 'Over', 'Yes', 'Chiefs', 'Chiefs', 'Bucs', 'Mahomes', 'Under', 'Yellow', 'The Hills', 'No', 'Teammates', 'Chiefs 30-26'],
['mitchell dzaldov', 'Over', 'Super Bowl', 'Under', 'Bruce Arians', 'Over', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Touchdown', 'Kelce', 'Hill', 'Chiefs', 'Chiefs', 'Butker', 'Mahomes', 'Chiefs', 'Brady', 'Jones', 'No', 'Yes', 'Kelce', 'Fournette', 'Under', 'Over', 'Under', 'Over', 'JPP', 'Godwin', 'Under', 'Under', 'Yes', 'Chiefs', 'Bucs', 'Bucs', 'Mahomes', 'Over', 'Clear', 'The Hills ', 'No', 'God', 'Chiefs 34-24'],
['Ambar', 'Over', 'Age', 'Over', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Chiefs', 'Pass', 'Touchdown', 'CEH', 'Brate', 'Chiefs', 'Bucs', 'Butker', 'Mahomes', 'Bucs', 'CEH', 'JPP', 'No', 'Yes', 'Hill', 'Fournette', 'Under', 'Under', 'Over', 'Over', 'Suh', 'Kelce', 'Over', 'Over', 'Yes', 'Chiefs', 'Chiefs', 'Bucs', 'Mahomes', 'Over', 'Orange', 'Star Boy', 'Yes', 'Family', 'Chiefs 41-28']]

df = pd.DataFrame(data, columns=['Name', 'Anthem over/under 1 minute and 59 Seconds (Jazmine Sullivan and Eric Church are singing)', 'What Will Be Verbally Mentioned/Alluded to First?', "How Many Times Will Gisele Bundchen (Brady's wife) Be Shown? (Post Game Broadcast DOESN'T Count) (Over/Under 1.5)", 'Who is shown first on TV during the national anthem', "Will the Total Points scored in the 1st half be Over/Under Jayson Tatum's Point Total vs. Suns of Feb. 7th", "Will Travis Kelce and Tyreek Hill combine to catch more balls than Russel Westbrooks' Assist total against the Hornets on Feb. 7th", 'Coin Toss', 'Which team wins the coin toss', 'First play type', 'First type of score', 'First Touchdown Scorer (3 points)', 'Last Touchdown Scorer (3 points)', 'Which team will score first', 'Which team will be the last to score?', 'Which player will hit the first field goal (Extra point DOES NOT count)', 'Which player will throw for more yards', 'First takeaway (Defensive team)', 'First player to commit a turnover (offensive player) (3 Points)', 'First player to cause a turnover (Defensive Player) (If it is a fumble, the player who caused the fumble) (3 points)', 'Will there be a safety', 'Will there be a defensive/special teams touchdown', 'Who will lead the game in receiving yards? (3 Points)', 'Who will lead the game in rushing yards? (3 Points)', 'Total sacks in the game (over/ under 4.5 )', 'Total turnovers in the game (over/under 2.5)', 'Total Penalties Accepted (over/under 12.5)', 'Longest Touchdown scored in the game (over/under 45.5 yards )', 'Player to Record the 1st Sack of the Game (2 points) ** If it is a half-sack 1 point will be awarded to each player involved', 'Player to Catch the 1st pass of the game (2 points)', 'Shortest Touchdown scored in the game (over/under 1.5 yards )', 'Longest FG scored in the game (over/under 47.5 yards )', 'Will there be a successful 2 Point Conversion', 'Who will be leading at halftime', 'Team to have First Coaches Challenge', 'Team to call First Timeout', 'Super bowl MVP? (3 points)', 'Total points (over/under 56.5)', 'Color of Gatorade bath on winning coach (2 Points)', 'First The Weekend Song (2 Points)', 'Will The Weekend Mention Canada During The Halftime Show', 'Who does the MVP thank first in the interview after he gets the award', 'Tie Breaker: Pick the winning team and the score of the game  (First tie break: Winning Team, Second tie break: Closest to Total Points Scored, Third Tie Break: 1 on 1 Flip Cup (full cup on zoom))'])
                  
def update_scores(df2, results):
    for index, row in df2.iterrows():
        count = 0
        for k in range(len(row.index)):

            if row.index[k] == "score":
                break
            if type(row.values[k]) == str and type(results.values[k]) == str:

                if row.values[k].lower() == results.values[k].lower():
                    if '3 points' in row.index[k].lower():
                        count += 3
                    elif '2 points' in row.index[k].lower():
                        count += 2
                    else:
                        count += 1
            else:
                if row.values[k] == results.values[k]:
                    if '3 points' in row.index[k].lower():
                        count += 3
                    elif '2 points' in row.index[k].lower():
                        count += 2
                    else:
                        count += 1

        df2["score"][index] = count

    return df2

def get_leader(df2):
    max_score = df2.shape[1]
    for i in range(max_score, 0, -1):
        if i in df2["score"].values:
            subdf = df2[df2["score"] == i]
            current_leader = subdf["Name"].values
            return current_leader

def get_scores_sorted(df2):
    sorted_scores = df2[["Name","score"]].sort_values(by=['score'], ascending=False)
    return sorted_scores.values

def update_results(results, item_to_update, value):
    if item_to_update == "" and value == "":
        return results
    results[item_to_update] = value
    return results

application = Flask(__name__)
df = df.dropna(subset=['Name'])
df2 = df.append(pd.Series(name="results"))
score = [0] * len(df2)
df2["score"] = score
scores = df2.loc["results"].fillna('N/A')


@application.route('/', methods=["GET", "POST"])
def hello():
    selected_value = ""
    result = ""
    data = df2
    results = scores
    #results = results.drop(['score', 'Paid'])
    keys = results.keys()
    selected_value = request.form.get('bets')
    result = request.form.get('result')
    # print(selected_value)
    # print(result)
    results = update_results(results, selected_value, result)
    data = update_scores(data, results)
    leaders = get_scores_sorted(data)
    keys = keys[0:len(keys)-2]
    results = results.values[0:len(results.values)-2]
    bet_results = zip(keys, results)
    return render_template('index.html', users = keys, leaders=leaders, results = bet_results)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)