# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 06:36 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **1/12** &nbsp;|&nbsp; Avg uptime: **82.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 50.0% | 1752.0 | 3715.3 | 1000ms | 4/8 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 374.9 | 1066.2 | 1500ms | 0/8 |
| ❌ | `catfact_random` | 87.5% | 50.0% | 2191.0 | 11306.7 | 3000ms | 4/8 |
| ❌ | `dog_ceo_random` | 100.0% | 37.5% | 1804.6 | 2754.4 | 2500ms | 5/8 |
| ❌ | `nasa_apod` | 100.0% | 75.0% | 1394.9 | 2584.9 | 2000ms | 2/8 |
| ❌ | `open_meteo_weather` | 100.0% | 50.0% | 1249.2 | 2181.6 | 2000ms | 4/8 |
| ❌ | `agify_name` | 100.0% | 50.0% | 1237.7 | 2819.7 | 2000ms | 4/8 |
| ❌ | `useless_fact` | 100.0% | 50.0% | 1195.4 | 2138.4 | 2500ms | 4/8 |
| ❌ | `rest_countries` | 100.0% | 50.0% | 1005.5 | 2163.1 | 2500ms | 4/8 |
| ❌ | `ipapi_check` | 100.0% | 62.5% | 841.3 | 1974.0 | 2500ms | 3/8 |
| ❌ | `jsonplaceholder_posts` | 100.0% | 50.0% | 791.4 | 2069.7 | 2000ms | 4/8 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 473.7 | 1095.5 | 1500ms | 0/8 |

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
