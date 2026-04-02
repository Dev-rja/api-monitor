# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 04:41 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **1/12** &nbsp;|&nbsp; Avg uptime: **81.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 0.0% | 3086.1 | 3715.3 | 1000ms | 4/4 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 692.2 | 1066.2 | 1500ms | 0/4 |
| ❌ | `catfact_random` | 75.0% | 0.0% | 4140.8 | 11306.7 | 800ms | 4/4 |
| ❌ | `dog_ceo_random` | 100.0% | 0.0% | 2270.2 | 2754.4 | 1000ms | 4/4 |
| ❌ | `agify_name` | 100.0% | 0.0% | 2090.1 | 2819.7 | 600ms | 4/4 |
| ❌ | `nasa_apod` | 100.0% | 75.0% | 1933.3 | 2169.1 | 2000ms | 1/4 |
| ❌ | `open_meteo_weather` | 100.0% | 0.0% | 1877.9 | 2181.6 | 1000ms | 4/4 |
| ❌ | `useless_fact` | 100.0% | 0.0% | 1812.6 | 2138.4 | 1000ms | 4/4 |
| ❌ | `rest_countries` | 100.0% | 0.0% | 1742.6 | 2163.1 | 1200ms | 4/4 |
| ❌ | `ipapi_check` | 100.0% | 25.0% | 1538.9 | 1974.0 | 1200ms | 3/4 |
| ❌ | `jsonplaceholder_posts` | 100.0% | 25.0% | 1185.0 | 2069.7 | 800ms | 3/4 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 820.4 | 1095.5 | 1500ms | 0/4 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 02:00 | 4140.8 | 100.0% |
| `numbers_trivia` | 02:00 | 3086.1 | 100.0% |
| `dog_ceo_random` | 02:00 | 2270.2 | 100.0% |
| `agify_name` | 02:00 | 2090.1 | 100.0% |
| `open_meteo_weather` | 02:00 | 1877.9 | 100.0% |
| `useless_fact` | 02:00 | 1812.6 | 100.0% |
| `rest_countries` | 02:00 | 1742.6 | 100.0% |
| `ipapi_check` | 02:00 | 1538.9 | 75.0% |
| `jsonplaceholder_posts` | 02:00 | 1185.0 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/your-username/api-monitor) via GitHub Actions + dbt._
