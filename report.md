# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 06:17 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **1/12** &nbsp;|&nbsp; Avg uptime: **81.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 33.33% | 2198.8 | 3715.3 | 1000ms | 4/6 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 483.4 | 1066.2 | 1500ms | 0/6 |
| ❌ | `catfact_random` | 83.33% | 33.33% | 2857.6 | 11306.7 | 800ms | 4/6 |
| ❌ | `dog_ceo_random` | 100.0% | 16.67% | 1927.3 | 2754.4 | 1000ms | 5/6 |
| ❌ | `nasa_apod` | 100.0% | 66.67% | 1779.8 | 2584.9 | 2000ms | 2/6 |
| ❌ | `agify_name` | 100.0% | 33.33% | 1494.8 | 2819.7 | 600ms | 4/6 |
| ❌ | `open_meteo_weather` | 100.0% | 33.33% | 1426.2 | 2181.6 | 1000ms | 4/6 |
| ❌ | `useless_fact` | 100.0% | 33.33% | 1389.3 | 2138.4 | 1000ms | 4/6 |
| ❌ | `rest_countries` | 100.0% | 33.33% | 1237.4 | 2163.1 | 1200ms | 4/6 |
| ❌ | `ipapi_check` | 100.0% | 50.0% | 1081.8 | 1974.0 | 1200ms | 3/6 |
| ❌ | `jsonplaceholder_posts` | 100.0% | 33.33% | 990.7 | 2069.7 | 800ms | 4/6 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 578.2 | 1095.5 | 1500ms | 0/6 |

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
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
