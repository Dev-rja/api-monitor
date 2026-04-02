# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 04:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **1/12** &nbsp;|&nbsp; Avg uptime: **81.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 20.0% | 2513.0 | 3715.3 | 1000ms | 4/5 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 567.7 | 1066.2 | 1500ms | 0/5 |
| ❌ | `catfact_random` | 80.0% | 20.0% | 3353.1 | 11306.7 | 800ms | 4/5 |
| ❌ | `dog_ceo_random` | 100.0% | 0.0% | 2130.9 | 2754.4 | 1000ms | 5/5 |
| ❌ | `nasa_apod` | 100.0% | 60.0% | 2063.7 | 2584.9 | 2000ms | 2/5 |
| ❌ | `agify_name` | 100.0% | 20.0% | 1710.3 | 2819.7 | 600ms | 4/5 |
| ❌ | `open_meteo_weather` | 100.0% | 20.0% | 1583.9 | 2181.6 | 1000ms | 4/5 |
| ❌ | `useless_fact` | 100.0% | 20.0% | 1536.6 | 2138.4 | 1000ms | 4/5 |
| ❌ | `rest_countries` | 100.0% | 20.0% | 1429.7 | 2163.1 | 1200ms | 4/5 |
| ❌ | `ipapi_check` | 100.0% | 40.0% | 1268.3 | 1974.0 | 1200ms | 3/5 |
| ❌ | `jsonplaceholder_posts` | 100.0% | 20.0% | 1143.2 | 2069.7 | 800ms | 4/5 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 670.5 | 1095.5 | 1500ms | 0/5 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 02:00 | 4140.8 | 100.0% |
| `numbers_trivia` | 02:00 | 3086.1 | 100.0% |
| `nasa_apod` | 04:00 | 2584.9 | 100.0% |
| `dog_ceo_random` | 02:00 | 2270.2 | 100.0% |
| `agify_name` | 02:00 | 2090.1 | 100.0% |
| `open_meteo_weather` | 02:00 | 1877.9 | 100.0% |
| `useless_fact` | 02:00 | 1812.6 | 100.0% |
| `rest_countries` | 02:00 | 1742.6 | 100.0% |
| `dog_ceo_random` | 04:00 | 1573.6 | 100.0% |
| `ipapi_check` | 02:00 | 1538.9 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/your-username/api-monitor) via GitHub Actions + dbt._
