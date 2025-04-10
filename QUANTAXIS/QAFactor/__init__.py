#
# The MIT License (MIT)
#
# Copyright (c) 2016-2021 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from QUANTAXIS.QAFactor.analyze import FactorAnalyzer
from QUANTAXIS.QAFactor.data import DataApi
from QUANTAXIS.QAFactor.fetcher import (QA_fetch_daily_basic,
                                        QA_fetch_financial_adv,
                                        QA_fetch_industry_adv,
                                        QA_fetch_last_financial,
                                        QA_fetch_stock_basic,
                                        QA_fetch_stock_name)
from QUANTAXIS.QAFactor.localize import (QA_ts_update_daily_basic,
                                         QA_ts_update_inc,
                                         QA_ts_update_industry,
                                         QA_ts_update_namechange)
from QUANTAXIS.QAFactor.preprocess import (QA_fetch_factor_weight,
                                           QA_fetch_get_factor_groupby,
                                           QA_fmt_factor,
                                           QA_standardize_factor,
                                           QA_winsorize_factor)
from QUANTAXIS.QAFactor.utils import QA_fmt_code_list
